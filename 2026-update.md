# vLLM and SGLang Performance Update (2026-10-13)

Why this update:  

1. The earlier tests were run almost a year ago, and both vLLM and SGLang have gone through many releases since then. 
2. The earlier tests also did not explicitly compare the vLLM V0 and V1 engines; this update tests both on vLLM 0.8.5.post1.
3.  The test hardware has also changed: the earlier tests used an NVIDIA A10, and this update uses an NVIDIA L20, so the numbers here are not directly comparable with the earlier A10 results. 

vLLM and SGLang now need separate environments: SGLang 0.5.21 requires `openai==2.6.1`, while the vLLM 0.31.0 environment has `openai` 3.29.0. In this update SGLang was installed in its own conda environment.

## Conclusion

On a single NVIDIA L20 running Qwen3-14B AWQ, vLLM 0.31.0 is faster than 0.8.5.post1:

- Against 0.8.5.post1 with the V1 engine (its default): completion tokens/s +16% to +19%, P95 latency 14% to 16% lower.
- Against 0.8.5.post1 with the V0 engine: completion tokens/s +22% to +31%, P95 latency 17% to 26% lower.
- The gap grows with concurrency.

In 2025 I reported the opposite on A10 + Qwen3-8B: 0.8.5.post1 was 16–17% faster than 0.10.x ([vllm#24082](https://github.com/vllm-project/vllm/issues/24082)). That regression no longer shows up with 0.31.0 in this setup.

SGLang 0.5.21 on the same setup:

- Its throughput falls between vLLM 0.8.5.post1 V1 and vLLM 0.31.0. vLLM 0.31.0 generated 3–5% more tokens/s at 10 concurrent requests and 6–9% more at 20 and 30.
- After every server start, the first batch of requests took about 60 seconds regardless of batch size (1, 10 or 20 requests). Later requests ran at normal speed. This also happened in a clean SGLang environment.

## Test Setup

**Hardware**

- NVIDIA L20 (46068 MiB visible), single card
- Driver 580.126.09, CUDA 13.0 (as reported by nvidia-smi)

**Software**

|                      | vLLM 0.31.0                    | vLLM 0.8.5.post1                |
| -------------------- | ------------------------------ | ------------------------------- |
| Environment          | own conda env (Python 3.12)    | own conda env (Python 3.12)     |
| PyTorch              | 2.13.0+cu130                   | 2.6.0 (required by 0.8.5.post1) |
| transformers         | as installed with vLLM         | 4.51.3                          |
| Attention backend    | FlashAttention                 | FlashAttention (V1 and V0)      |
| Top-p/top-k sampling | default (FlashInfer installed) | PyTorch-native (see below)      |

Test client: `qwen3_openai_stress_test.py`, OpenAI-compatible Chat Completions API, run from the same environment for all tests.

**Model**: Qwen3-14B AWQ (`quantization=awq_marlin`, weights 9.36 GiB)

**Server command** (identical for both vLLM versions)

```bash
vllm serve /home/vllm/llm/Qwen/Qwen3-14B \
  --served-model-name qwen3-14b \
  --port 8000 \
  --max-model-len 8192 \
  --tensor-parallel-size 1 \
  --max-num-seqs 40

# V0 engine on 0.8.5.post1
VLLM_USE_V1=0 vllm serve ... (same arguments)
```

Engine confirmed from startup logs: `Initializing a V1 LLM engine (v0.8.5.post1)` for V1; V0 modules (`llm_engine.py`, `model_runner.py`) for V0. KV cache on 0.8.5.post1: 195,136 tokens (V1), 192,672 tokens (V0); demand at 30 concurrent requests is under 10k tokens.

**Request parameters**

- `max_tokens=256`, `temperature=0.7`
- Thinking disabled per request: `--enable-thinking false`
- 20 prompts chosen at random; total requests = 10 × concurrency
- Token counts from `usage.completion_tokens`
- One warm-up round after each server start, not recorded

**SGLang**

- SGLang 0.5.21, own conda environment as officially required (`openai==2.6.1`), PyTorch 2.13.0+cu130
- Some runs used an earlier install inside the vLLM environment ("shared env" below); results differed from the clean install by less than 2%

```bash
python -m sglang.launch_server \
  --model-path /home/vllm/llm/Qwen/Qwen3-14B \
  --served-model-name qwen3-14b \
  --host 0.0.0.0 \
  --port 8000 \
  --tp 1 \
  --context-length 8192
```

`--mem-fraction-static` left at default (setting it to 0.85 made startup hang while capturing CUDA graphs). SGLang reported `max_total_num_tokens=181310` and `max_running_requests=4096`. Neither vLLM nor SGLang used `--reasoning-parser`.

## vLLM Results

### Completion tokens per second

| Concurrency | 0.8.5.post1 V0 | 0.8.5.post1 V1 | 0.31.0  | V0 → V1 | 0.8.5 V1 → 0.31.0 | V0 → 0.31.0 |
| ----------- | -------------- | -------------- | ------- | ------- | ----------------- | ----------- |
| 10          | 571            | 597–604        | 695–699 | +5%     | +16%              | +22%        |
| 20          | 1002           | 1086–1094      | 1276    | +9%     | +17%              | +27%        |
| 30          | 1385           | 1527           | 1818    | +10%    | +19%              | +31%        |

### P95 response time

| Concurrency | 0.8.5.post1 V0 | 0.8.5.post1 V1 | 0.31.0      |
| ----------- | -------------- | -------------- | ----------- |
| 10          | 4.31 s         | 4.10–4.13 s    | 3.55–3.56 s |
| 20          | 5.01 s         | 4.58 s         | 3.88 s      |
| 30          | 5.56 s         | 4.89 s         | 4.09 s      |

### 0.8.5.post1 sampling implementation

vLLM 0.8.5.post1 disables FlashInfer top-p/top-k sampling when FlashInfer ≥ 0.2.3 is installed and falls back to PyTorch-native sampling. With FlashInfer 0.2.2.post1 (`+cu124torch2.6` prebuilt wheel) the FlashInfer sampler is enabled, and it was slower:

| Concurrency | Metric     | PyTorch-native | FlashInfer 0.2.2.post1 | FlashInfer slower by |
| ----------- | ---------- | -------------- | ---------------------- | -------------------- |
| 10          | P95        | 4.10 s         | 4.99 s                 | ~22%                 |
|             | Throughput | 2.47 req/s     | 2.05 req/s             | ~17%                 |
| 20          | P95        | 4.58 s         | 5.41 s                 | ~18%                 |
|             | Throughput | 4.69 req/s     | 3.80 req/s             | ~19%                 |
| 30          | P95        | 4.89 s         | 5.75 s                 | ~18%                 |
|             | Throughput | 6.37 req/s     | 5.43 req/s             | ~15%                 |

The 0.8.5.post1 results in the comparison above use PyTorch-native sampling.

### Raw Data

| Version / engine | Sampling                              | Concurrency / Total | P95 (s) | Avg (s) | Throughput (req/s) | Tokens/s | Avg tokens/req |
| ---------------- | ------------------------------------- | ------------------- | ------- | ------- | ------------------ | -------- | -------------- |
| 0.31.0           | default                               | 10 / 100            | 3.55    | 3.34    | 2.85               | 694.77   | 243.54         |
| 0.31.0           | default                               | 10 / 100            | 3.56    | 3.38    | 2.85               | 699.43   | 245.74         |
| 0.31.0           | default                               | 20 / 200            | 3.88    | 3.66    | 5.23               | 1275.94  | 244.11         |
| 0.31.0           | default                               | 30 / 300            | 4.09    | 3.89    | 7.41               | 1817.81  | 245.21         |
| 0.8.5.post1 V1   | PyTorch (FlashInfer ≥0.2.3 installed) | 10 / 100            | 4.10    | 3.86    | 2.47               | 603.92   | 244.25         |
| 0.8.5.post1 V1   | PyTorch (FlashInfer ≥0.2.3 installed) | 20 / 200            | 4.58    | 4.05    | 4.69               | 1085.80  | 231.33         |
| 0.8.5.post1 V1   | PyTorch (FlashInfer ≥0.2.3 installed) | 30 / 300            | 4.89    | 4.48    | 6.37               | 1526.74  | 239.80         |
| 0.8.5.post1 V1   | PyTorch (no FlashInfer)               | 10 / 100            | 4.13    | 3.83    | 2.47               | 597.49   | 241.87         |
| 0.8.5.post1 V1   | PyTorch (no FlashInfer)               | 20 / 200            | 4.58    | 4.29    | 4.48               | 1094.27  | 244.45         |
| 0.8.5.post1 V1   | FlashInfer 0.2.2.post1                | 10 / 100            | 4.99    | 4.57    | 2.05               | 487.25   | 237.80         |
| 0.8.5.post1 V1   | FlashInfer 0.2.2.post1                | 20 / 200            | 5.41    | 5.01    | 3.80               | 913.20   | 240.37         |
| 0.8.5.post1 V1   | FlashInfer 0.2.2.post1                | 30 / 300            | 5.75    | 5.25    | 5.43               | 1291.33  | 237.72         |
| 0.8.5.post1 V0   | PyTorch (no FlashInfer)               | 10 / 100            | 4.31    | 4.05    | 2.36               | 571.27   | 242.53         |
| 0.8.5.post1 V0   | PyTorch (no FlashInfer)               | 20 / 200            | 5.01    | 4.57    | 4.19               | 1002.32  | 239.46         |
| 0.8.5.post1 V0   | PyTorch (no FlashInfer)               | 30 / 300            | 5.56    | 5.02    | 5.71               | 1384.76  | 242.39         |

The first 0.31.0 run at 10 concurrency disabled thinking with a custom non-thinking chat template instead of the per-request flag; results matched the second run.

## SGLang 0.5.21

### Comparison with vLLM (after warm-up)

| Concurrency | Metric     | vLLM 0.8.5.post1 V1 | SGLang 0.5.21   | vLLM 0.31.0 |
| ----------- | ---------- | ------------------- | --------------- | ----------- |
| 10          | P95        | 4.10–4.13 s         | 3.68–3.78 s     | 3.55–3.56 s |
|             | Throughput | 2.47 req/s          | 2.77–2.78 req/s | 2.85 req/s  |
|             | Tokens/s   | 597–604             | 666–680         | 695–699     |
| 20          | P95        | 4.58 s              | 4.24–4.31 s     | 3.88 s      |
|             | Throughput | 4.48–4.69 req/s     | 4.93–5.01 req/s | 5.23 req/s  |
|             | Tokens/s   | 1086–1094           | 1168–1187       | 1276        |
| 30          | P95        | 4.89 s              | 4.46–4.49 s     | 4.09 s      |
|             | Throughput | 6.37 req/s          | 6.99–7.10 req/s | 7.41 req/s  |
|             | Tokens/s   | 1527                | 1687–1711       | 1818        |

SGLang at 10 concurrency was tested only in the shared environment.

### Warm-up

| Run                                     | First batch size | Slowest request | Median | Total duration          |
| --------------------------------------- | ---------------- | --------------- | ------ | ----------------------- |
| First request after start (thinking on) | 1                | 58.18 s         | –      | 58.19 s                 |
| Second request (thinking off)           | 1                | 7.82 s          | –      | 7.84 s                  |
| Restart, shared env, 10 / 100           | 10               | 63.28 s         | 3.66 s | 95.56 s (normal: ~36 s) |
| First start, own env, 20 / 200          | 20               | 58.99 s         | 4.07 s | 99.60 s (normal: ~40 s) |

Both single requests generated 256 tokens. In the two batch runs, P90 was 56.43 s and 58.97 s respectively, so the slow requests were the first batch; the rest ran at normal speed.

Server startup itself: CUDA graph capture for prefill took 214.78 s, total engine startup about 229 s.

No comparable first-batch slowdown appeared in the recorded vLLM runs.

#### Raw output

```
Test completed in 58.19 seconds
         LLM Stress Test Results - 2026-10-13 11:14:51
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ qwen3-14b                │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 10                       │
│ Total Requests                    │ 1                        │
│ Successful Requests               │ 1 (100.0%)               │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 58.19 seconds            │
│ Min Response Time                 │ 58.18 seconds            │
│ Max Response Time                 │ 58.18 seconds            │
│ Average Response Time             │ 58.18 seconds            │
│ Median Response Time              │ 58.18 seconds            │
│ P90 Response Time                 │ 58.18 seconds            │
│ P95 Response Time                 │ 58.18 seconds            │
│ P99 Response Time                 │ 58.18 seconds            │
│ Theoretical Max Throughput        │ 0.02 requests/second     │
│ Actual Throughput                 │ 0.02 requests/second     │
│ Total Completion Tokens           │ 256                      │
│ Total Prompt Tokens               │ 16                       │
│ Total Tokens                      │ 272                      │
│ Completion Tokens Per Second      │ 4.40                     │
│ Avg Completion Tokens Per Request │ 256.00                   │
│ Peak Requests In Flight           │ 1                        │
└───────────────────────────────────┴──────────────────────────┘

Test completed in 7.84 seconds
         LLM Stress Test Results - 2026-10-13 11:19:55
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ qwen3-14b                │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ False                    │
│ Concurrent Requests               │ 10                       │
│ Total Requests                    │ 1                        │
│ Successful Requests               │ 1 (100.0%)               │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 7.84 seconds             │
│ Min Response Time                 │ 7.82 seconds             │
│ Max Response Time                 │ 7.82 seconds             │
│ Average Response Time             │ 7.82 seconds             │
│ Median Response Time              │ 7.82 seconds             │
│ P90 Response Time                 │ 7.82 seconds             │
│ P95 Response Time                 │ 7.82 seconds             │
│ P99 Response Time                 │ 7.82 seconds             │
│ Theoretical Max Throughput        │ 0.13 requests/second     │
│ Actual Throughput                 │ 0.13 requests/second     │
│ Total Completion Tokens           │ 256                      │
│ Total Prompt Tokens               │ 21                       │
│ Total Tokens                      │ 277                      │
│ Completion Tokens Per Second      │ 32.66                    │
│ Avg Completion Tokens Per Request │ 256.00                   │
│ Peak Requests In Flight           │ 1                        │
└───────────────────────────────────┴──────────────────────────┘

Test completed in 95.56 seconds
         LLM Stress Test Results - 2026-10-13 11:32:25
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ qwen3-14b                │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ False                    │
│ Concurrent Requests               │ 10                       │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 95.56 seconds            │
│ Min Response Time                 │ 1.16 seconds             │
│ Max Response Time                 │ 63.28 seconds            │
│ Average Response Time             │ 9.38 seconds             │
│ Median Response Time              │ 3.66 seconds             │
│ P90 Response Time                 │ 56.43 seconds            │
│ P95 Response Time                 │ 63.27 seconds            │
│ P99 Response Time                 │ 63.28 seconds            │
│ Std Dev Response Time             │ 17.78 seconds            │
│ Theoretical Max Throughput        │ 1.58 requests/second     │
│ Actual Throughput                 │ 1.05 requests/second     │
│ Total Completion Tokens           │ 23967                    │
│ Total Prompt Tokens               │ 2230                     │
│ Total Tokens                      │ 26197                    │
│ Completion Tokens Per Second      │ 250.81                   │
│ Avg Completion Tokens Per Request │ 239.67                   │
│ Peak Requests In Flight           │ 10                       │
└───────────────────────────────────┴──────────────────────────┘

Test completed in 99.60 seconds
         LLM Stress Test Results - 2026-10-13 12:04:36
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ qwen3-14b                │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ False                    │
│ Concurrent Requests               │ 20                       │
│ Total Requests                    │ 200                      │
│ Successful Requests               │ 200 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 99.60 seconds            │
│ Min Response Time                 │ 1.32 seconds             │
│ Max Response Time                 │ 58.99 seconds            │
│ Average Response Time             │ 9.80 seconds             │
│ Median Response Time              │ 4.07 seconds             │
│ P90 Response Time                 │ 58.97 seconds            │
│ P95 Response Time                 │ 58.97 seconds            │
│ P99 Response Time                 │ 58.98 seconds            │
│ Std Dev Response Time             │ 16.49 seconds            │
│ Theoretical Max Throughput        │ 3.39 requests/second     │
│ Actual Throughput                 │ 2.01 requests/second     │
│ Total Completion Tokens           │ 48972                    │
│ Total Prompt Tokens               │ 4481                     │
│ Total Tokens                      │ 53453                    │
│ Completion Tokens Per Second      │ 491.70                   │
│ Avg Completion Tokens Per Request │ 244.86                   │
│ Peak Requests In Flight           │ 20                       │
└───────────────────────────────────┴──────────────────────────┘
```

### Raw Data

| Env    | Concurrency / Total | P95 (s) | Avg (s) | Std Dev (s) | Throughput (req/s) | Tokens/s | Avg tokens/req |
| ------ | ------------------- | ------- | ------- | ----------- | ------------------ | -------- | -------------- |
| shared | 10 / 100            | 3.78    | 3.41    | –           | 2.77               | 665.74   | 240.60         |
| shared | 10 / 100            | 3.68    | 3.44    | 0.54        | 2.78               | 680.39   | 244.33         |
| shared | 20 / 200            | 4.31    | 3.86    | 0.75        | 4.93               | 1167.75  | 236.90         |
| own    | 20 / 200            | 4.24    | 3.81    | 0.78        | 5.01               | 1187.33  | 237.18         |
| shared | 30 / 300            | 4.49    | 4.09    | 0.74        | 6.99               | 1686.75  | 241.34         |
| own    | 30 / 300            | 4.46    | 4.03    | 0.70        | 7.10               | 1711.46  | 240.92         |

## Scope

Most responses reached the 256-token limit and prompts were about 22 tokens, so these results cover short, fixed-length outputs with very short inputs, measured as full (non-streaming) response time. Long outputs, long prompts such as RAG context, and time to first token were not tested.