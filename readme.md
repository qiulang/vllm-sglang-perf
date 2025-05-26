# SGLang vs vLLM Performance Comparison: An Initial Assessment

## Table of Contents
- [Introduction](#introduction)
- [Test Setup](#test-setup)
- [Key Findings](#key-findings)
- [Single-GPU Results](#single-gpu-results)
- [Multi-GPU Results](#multi-gpu-results)
- [Parameter Equivalence Discovery](#parameter-equivalence-discovery)
- [Performance Analysis](#performance-analysis)
- [Warm-up Effect](#warm-up-effect)
- [Limitations and Suggestions](#limitations-and-suggestions)
- [Testing Scripts](#testing-scripts)
- [Running Your Own Tests](#running-your-own-tests)
- [Important Notes on Performance Testing](#important-notes-on-performance-testing)
- [Conclusion](#conclusion)
- [Appendix for Qwen3-4B](#Appendix-Qwen3-4B)
- [Quick Recommendation](#Quick-Recommendation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

[SGLang](https://github.com/sgl-project/sglang) and [vLLM](https://github.com/vllm-project/vllm) are both high-performance inference frameworks for large language models, with SGLang taking a compilation-based approach while vLLM focuses on optimized attention and memory management.

Before starting this comparison, I had no bias toward either framework and was simply curious about their relative performance. I understand benchmark testing without clear objectives can often be misleading and produce non-objective results. However, this project has a specific, focused goal: to evaluate how vLLM and SGLang perform when running a small LLM model on a **mid-range** NVIDIA GPU like **A10**, in both single and multi-GPU configurations.

It's worth noting that official benchmarks from vLLM against SGLang exist (https://blog.vllm.ai/2024/09/05/perf-update.html), but these were conducted in September 2024 on high-end A100 and H100 GPUs. Our testing on mid-range A10 GPUs in April 2025 reflects different hardware profiles and more recent versions of both frameworks. The LLM inference landscape evolves rapidly, with both frameworks receiving regular updates that can significantly change performance characteristics. This highlights the importance of testing with your specific hardware, models, and the latest framework versions rather than relying solely on existing benchmarks.

For this test, I selected the [Qwen 2.5 7B quantized model](https://modelscope.cn/models/Qwen/Qwen2.5-7B-Instruct-AWQ/). I specifically chose its AWQ variant rather than the GPTQ int 4-bit model, based on both information from sources like https://github.com/mit-han-lab/llm-awq and my own testing, which showed AWQ outperforming GPTQ int 4-bit models.

This represents a practical, real-world scenario for organizations deploying smaller quantized models on accessible hardware, rather than focusing on high-end multi-GPU setups that may be less common in production environments.

The comparative analysis revealed important nuances about configuration impacts, with each framework exhibiting specific performance advantages in different deployment scenarios depending on parallelism strategies and parameter settings.

### Qwen3 upate

Following the release of [Qwen3](https://qwenlm.github.io/blog/qwen3/) quantization models in May 2025, I conducted additional performance testing using [Qwen3-4B AWQ](https://modelscope.cn/models/Qwen/Qwen3-4B-AWQ) with the same hardware configuration as the original tests.

The results significantly challenged my initial conclusions from the Qwen2.5-7B testing. While SGLang demonstrated clear advantages for Qwen2.5-7B through extremely consistent response times and excellent throughput (accounting for the initial warm-up phase and steeper learning curve), **vLLM emerged as the superior choice for Qwen3-4B** with better consistency, throughput, and overall performance characteristics.

This finding aligns with Qwen's official deployment recommendations. Their [documentation](https://qwen.readthedocs.io/en/latest/deployment/vllm.html) explicitly states: *"We recommend you trying [vLLM](https://github.com/vllm-project/vllm) for your deployment of Qwen,"* while SGLang receives only [a brief mention](https://qwen.readthedocs.io/en/latest/deployment/sglang.html) as *"a fast serving framework for large language models and vision language models."*

However, reaching this conclusion required extensive testing and multiple iterations to uncover critical methodological issues, including fundamental differences in parameter handling between frameworks. The detailed analysis in the Appendix reveals why initial performance comparisons were misleading and provides crucial insights for accurate framework evaluation.

## Test Setup

### Hardware
- Single, dual and quad [NVIDIA A10 GPU (24GB)](https://www.nvidia.com/en-us/data-center/products/a10-gpu/) configurations
- Intel® Xeon® Gold 6326 Processor, **30** GiB memory

### Software
- Ubuntu 22, GPU Driver 550.127.08/CUDA 12.4.1/CUDNN 9.2.0.82
- Conda 23.7.4, python 3.12
- SGLang (version 0.4.5 latest, `pip install "sglang[all]>=0.4.5.post3"` )
- vLLM (version v0.8.4 latest, `pip install vllm`)
- Model: [Qwen2.5 7B-AWQ (quantized)](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ)

### Test Parameters
- Requests: 20 (small test) and 300 (larger test), single-round inference
- Concurrency: 5 and 30 concurrent requests
- Identical prompts with max_tokens=256

### Test workflow

1. Setup:
   - Started with a clean Ubuntu 22 machine with only CUDA & Conda environments installed
   - No other GPU processes running during tests as nvidia-smi shows.

2. First SGLang testing:
   - Start the SGLang server, `python3 -m sglang.launch_server --model-path $MODEL_PATH --context-length 8192 --tp 1|2|4`
   - Run the SGLang stress test script (which is provided as-is and may benefit from further refinement)
   - Record the performance metrics

3. For vLLM testing:
   - Stop the SGLang server
   - Start the vLLM server, `vllm serve $MODEL_PATH --max-model-len 8192 --tensor-parallel-size 1|2|4`
   - Run the vLLM stress test script
   - Record the performance metrics

4. Repeat for both single, dual, quad GPU configurations

## Key Findings

1. **In single-GPU scenarios**: SGLang demonstrated extremely consistent response times, higher throughput, and comparable memory usage when properly configured.

2. **In multi-GPU scenarios**: vLLM maintained consistent performance while SGLang showed significant variability and decreased throughput when using the `--dp` (**data parallelism**) flag.

3. **Unexpected parallelism impact**: When switching SGLang from data parallelism (`--dp`) to **tensor parallelism** (`--tp`), performance dramatically improved on multi-GPU setups, restoring **the consistency and throughput advantages** seen in single-GPU scenarios. This parallelism strategy choice had a much larger impact on performance characteristics than expected.

4. **Warm-up differences**: SGLang showed a significant "warm-up effect" requiring initial requests to reach optimal performance, while vLLM delivered consistent performance from the first request without warm-up.

5. **Unanswered question**: Why does tensor parallelism in SGLang provide such dramatically better performance consistency than data parallelism for a model that easily fits on a single GPU? This counter-intuitive finding invites further investigation from the community. [The SGLang document](https://docs.sglang.ai/backend/server_arguments.html) may provide some clues,"Data parallelism is better for throughput if there is enough memory. It can also be used together with tensor parallelism. We recommend [SGLang Router](https://docs.sglang.ai/router/router.html) for data parallelism."

   

## Single-GPU Results

### Memory Usage

| Metric                     | SGLang          | vLLM           |
| -------------------------- | --------------- | -------------- |
| Memory Usage               | 20996 MiB (91%) | 21058MiB (91%) |
| GPU Utilization            | 92%             | 93%            |
| Power Consumption          | 151W            | 145W           |
| Temperature                | 49°C            | 50°C           |
| Throughput (30 concurrent) | 14.92 req/s     | 9.50 req/s     |

### Performance Metrics
- **Response Time Consistency**: SGLang demonstrated remarkably consistent response times (std dev of just 0.01s)
- **Throughput**: SGLang achieved ~57% higher throughput than vLLM
- **GPU Utilization**: Both frameworks utilized the GPU efficiently (91-95%)

### Single-GPU Test Results Summary

#### SGLang for 5 Concurrent Requests (20 total)

```
Test completed in 6.05 seconds
        SGLang Stress Test Results - 2025-04-25 21:27:57        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 5                               │
│ Total Requests             │ 20                              │
│ Successful Requests        │ 20 (100.0%)                     │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 6.05 seconds                    │
│ Min Response Time          │ 1.51 seconds                    │
│ Max Response Time          │ 1.52 seconds                    │
│ Average Response Time      │ 1.51 seconds                    │
│ Median Response Time       │ 1.51 seconds                    │
│ P90 Response Time          │ 1.52 seconds                    │
│ P95 Response Time          │ 1.52 seconds                    │
│ P99 Response Time          │ 1.52 seconds                    │
│ Std Dev Response Time      │ 0.01 seconds                    │
│ Theoretical Max Throughput │ 13.16 requests/second           │
│ Actual Throughput          │ 3.31 requests/second            │
│ Total Generated Tokens     │ 2014                            │
│ Tokens Per Second          │ 333.00                          │
│ Avg Tokens Per Request     │ 100.70                          │
│ Peak Requests In Flight    │ 5                               │
└────────────────────────────┴─────────────────────────────────┘
```

#### vLLM for 5 Concurrent Requests (20 total)

```
Test completed in 7.56 seconds
           vLLM Stress Test Results - 2025-04-25 22:08:34            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:8000/v1/completions │
│ Model                      │ /home/vllm/llm/Qwen7B-awq            │
│ Max Tokens                 │ 256                                  │
│ Temperature                │ 0.7                                  │
│ Concurrent Requests        │ 5                                    │
│ Total Requests             │ 20                                   │
│ Successful Requests        │ 20 (100.0%)                          │
│ Failed Requests            │ 0 (0.0%)                             │
│ Total Test Duration        │ 7.56 seconds                         │
│ Min Response Time          │ 1.33 seconds                         │
│ Max Response Time          │ 2.19 seconds                         │
│ Average Response Time      │ 1.64 seconds                         │
│ Median Response Time       │ 1.62 seconds                         │
│ P90 Response Time          │ 1.97 seconds                         │
│ P95 Response Time          │ 2.19 seconds                         │
│ P99 Response Time          │ 2.19 seconds                         │
│ Std Dev Response Time      │ 0.20 seconds                         │
│ Theoretical Max Throughput │ 9.12 requests/second                 │
│ Actual Throughput          │ 2.65 requests/second                 │
│ Total Generated Tokens     │ 1961                                 │
│ Tokens Per Second          │ 259.53                               │
│ Avg Tokens Per Request     │ 98.05                                │
│ Peak Requests In Flight    │ 5                                    │
└────────────────────────────┴──────────────────────────────────────┘
```

Refer to the complete result [here](./OneA10-test-result-samples.md)

### Single-GPU Comparison

#### 5 Concurrent Requests (20 total)
| Metric | SGLang | vLLM |
|--------|--------|------|
| Avg Response Time | 1.51s | 1.64s |
| Std Dev | 0.01s | 0.20s |
| Throughput | 3.31 req/s | 2.65 req/s |

#### 30 Concurrent Requests (300 total)
| Metric | SGLang | vLLM |
|--------|--------|------|
| Avg Response Time | 2.01s | 2.57s |
| Std Dev | 0.05s | 0.30s |
| Throughput | 14.92 req/s | 9.50 req/s |
| Token Generation | 1544.94 tok/s | 961.05 tok/s |

## Multi-GPU Results

For SGLang, the choice between data parallelism (DP) and tensor parallelism (TP) has a major impact on performance characteristics

### The Parallelism Strategy Discovery

Initially, SGLang was configured with the `--dp` flag (data parallelism) for multi-GPU tests, based on my assumption that data parallelism is better for throughput when there's enough memory, refer to https://docs.sglang.ai/backend/server_arguments.html. The Qwen 7B model easily fits on a single A10 GPU's 24GB memory, so this seemed like the right choice.

However, after observing surprisingly poor performance with data parallelism, I got the feedback from https://github.com/sgl-project/sglang/issues/5808 that I should use `tp` flag instead.

This resulted in dramatically improved performance, with consistency and throughput comparable to or better than the single-GPU results.

**What happened?**

1. **Data Parallelism (`--dp`)**: When using this approach, each GPU gets a complete copy of the model and handles separate batches independently. While this increases theoretical throughput capacity, it led to highly variable response times and less efficient request processing in practice.
2. **Tensor Parallelism (`--tp`)**: With this approach, a single model is split across multiple GPUs, with each GPU handling a portion of the model's computation. For our Qwen 7B model, this provided much more consistent response times and better overall throughput.

This finding challenges my idea about when to use tensor vs. data parallelism. While tensor parallelism is often recommended primarily for models too large to fit on a single GPU, our testing demonstrates it can also be superior for smaller models when consistent response times and efficient multi-GPU scaling are priorities.

### SGLang with Data Parallelism

When testing SGLang on 2 A10 GPUs using the `--dp` (data parallelism) flag, the performance degraded significantly compared to single-GPU operation:

#### SGLang with 30 Concurrent Requests (300 total)

```
Test completed in 36.91 seconds
        SGLang Stress Test Results - 2025-04-27 14:00:37        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 36.91 seconds                   │
│ Min Response Time          │ 1.55 seconds                    │
│ Max Response Time          │ 8.58 seconds                    │
│ Average Response Time      │ 3.23 seconds                    │
│ Median Response Time       │ 2.31 seconds                    │
│ P90 Response Time          │ 8.53 seconds                    │
│ P95 Response Time          │ 8.55 seconds                    │
│ P99 Response Time          │ 8.58 seconds                    │
│ Std Dev Response Time      │ 1.94 seconds                    │
│ Theoretical Max Throughput │ 34.97 requests/second           │
│ Actual Throughput          │ 8.13 requests/second            │
│ Total Generated Tokens     │ 31515                           │
│ Tokens Per Second          │ 853.94                          │
│ Avg Tokens Per Request     │ 105.05                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘
```

#### Another SGLang run showing even higher variance:

```
Test completed in 60.97 seconds
        SGLang Stress Test Results - 2025-04-27 14:10:34        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 60.97 seconds                   │
│ Min Response Time          │ 1.52 seconds                    │
│ Max Response Time          │ 12.37 seconds                   │
│ Average Response Time      │ 4.44 seconds                    │
│ Median Response Time       │ 3.81 seconds                    │
│ P90 Response Time          │ 6.30 seconds                    │
│ P95 Response Time          │ 11.51 seconds                   │
│ P99 Response Time          │ 12.37 seconds                   │
│ Std Dev Response Time      │ 2.37 seconds                    │
│ Theoretical Max Throughput │ 24.26 requests/second           │
│ Actual Throughput          │ 4.92 requests/second            │
│ Total Generated Tokens     │ 31214                           │
│ Tokens Per Second          │ 511.92                          │
│ Avg Tokens Per Request     │ 104.05                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴──────────────────────────────── │

```

### SGLang with Tensor Parallelism

When switching to tensor parallelism using the `--tp` flag, SGLang's performance on 2 GPUs dramatically improved, showing similar characteristics to its single-GPU performance:

```
Test completed in 26.97 seconds
        SGLang Stress Test Results - 2025-04-28 23:17:05        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 26.97 seconds                   │
│ Min Response Time          │ 2.68 seconds                    │
│ Max Response Time          │ 2.78 seconds                    │
│ Average Response Time      │ 2.69 seconds                    │
│ Median Response Time       │ 2.68 seconds                    │
│ P90 Response Time          │ 2.78 seconds                    │
│ P95 Response Time          │ 2.78 seconds                    │
│ P99 Response Time          │ 2.78 seconds                    │
│ Std Dev Response Time      │ 0.03 seconds                    │
│ Theoretical Max Throughput │ 107.73 requests/second          │
│ Actual Throughput          │ 11.12 requests/second           │
│ Total Generated Tokens     │ 31221                           │
│ Tokens Per Second          │ 1157.76                         │
│ Avg Tokens Per Request     │ 104.07                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 26.93 seconds
        SGLang Stress Test Results - 2025-04-28 23:17:38        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 26.93 seconds                   │
│ Min Response Time          │ 2.68 seconds                    │
│ Max Response Time          │ 2.70 seconds                    │
│ Average Response Time      │ 2.69 seconds                    │
│ Median Response Time       │ 2.69 seconds                    │
│ P90 Response Time          │ 2.70 seconds                    │
│ P95 Response Time          │ 2.70 seconds                    │
│ P99 Response Time          │ 2.70 seconds                    │
│ Std Dev Response Time      │ 0.01 seconds                    │
│ Theoretical Max Throughput │ 111.07 requests/second          │
│ Actual Throughput          │ 11.14 requests/second           │
│ Total Generated Tokens     │ 31008                           │
│ Tokens Per Second          │ 1151.33                         │
│ Avg Tokens Per Request     │ 103.36                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

```

### vLLM Multi-GPU Results

For comparison, vLLM's results on 2 A10 GPUs:

```
           vLLM Stress Test Results - 2025-04-27 14:26:27            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:8000/v1/completions │
│ Model                      │ /home/vllm/llm/Qwen7B-awq            │
│ Max Tokens                 │ 256                                  │
│ Temperature                │ 0.7                                  │
│ Concurrent Requests        │ 30                                   │
│ Total Requests             │ 300                                  │
│ Successful Requests        │ 300 (100.0%)                         │
│ Failed Requests            │ 0 (0.0%)                             │
│ Total Test Duration        │ 27.73 seconds                        │
│ Min Response Time          │ 1.34 seconds                         │
│ Max Response Time          │ 2.97 seconds                         │
│ Average Response Time      │ 2.26 seconds                         │
│ Median Response Time       │ 2.28 seconds                         │
│ P90 Response Time          │ 2.62 seconds                         │
│ P95 Response Time          │ 2.71 seconds                         │
│ P99 Response Time          │ 2.85 seconds                         │
│ Std Dev Response Time      │ 0.27 seconds                         │
│ Theoretical Max Throughput │ 101.01 requests/second               │
│ Actual Throughput          │ 10.82 requests/second                │
│ Total Generated Tokens     │ 29779                                │
│ Tokens Per Second          │ 1074.01                              │
│ Avg Tokens Per Request     │ 99.26                                │
│ Peak Requests In Flight    │ 30                                   │
└────────────────────────────┴──────────────────────────────────────┘
```

#### Another vLLM run showing similar consistency on 2 A10

```
Test completed in 29.73 seconds
           vLLM Stress Test Results - 2025-04-27 14:25:12            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:8000/v1/completions │
│ Model                      │ /home/vllm/llm/Qwen7B-awq            │
│ Max Tokens                 │ 256                                  │
│ Temperature                │ 0.7                                  │
│ Concurrent Requests        │ 30                                   │
│ Total Requests             │ 300                                  │
│ Successful Requests        │ 300 (100.0%)                         │
│ Failed Requests            │ 0 (0.0%)                             │
│ Total Test Duration        │ 29.72 seconds                        │
│ Min Response Time          │ 1.23 seconds                         │
│ Max Response Time          │ 3.62 seconds                         │
│ Average Response Time      │ 2.32 seconds                         │
│ Median Response Time       │ 2.35 seconds                         │
│ P90 Response Time          │ 2.60 seconds                         │
│ P95 Response Time          │ 2.70 seconds                         │
│ P99 Response Time          │ 3.32 seconds                         │
│ Std Dev Response Time      │ 0.28 seconds                         │
│ Theoretical Max Throughput │ 82.83 requests/second                │
│ Actual Throughput          │ 10.09 requests/second                │
│ Total Generated Tokens     │ 30492                                │
│ Tokens Per Second          │ 1025.81                              │
│ Avg Tokens Per Request     │ 101.64                               │
│ Peak Requests In Flight    │ 30                                   │
└────────────────────────────┴──────────────────────────────────────┘
```

### 2-GPU Comparison with Corrected Parallelism Strategy (30 concurrent requests)

| Metric                | SGLang (DP)     | SGLang (TP)       | vLLM        |
| --------------------- | --------------- | ----------------- | ----------- |
| Min Response Time     | 1.52-1.55s      | 2.68s             | 1.34s       |
| Max Response Time     | 8.58-12.37s     | 2.70-2.78s        | 2.97s       |
| Average Response Time | 3.23-4.44s      | 2.69s             | 2.26s       |
| Std Dev Response Time | 1.94-2.37s      | 0.01-0.03s        | 0.27s       |
| Actual Throughput     | 4.92-8.13 req/s | 11.12-11.14 req/s | 10.82 req/s |
| Tokens Per Second     | 511-853         | 1151-1158         | 1074        |

What's particularly impressive is that SGLang with tensor parallelism (although vllm has better min reponse times):

1. Shows almost perfect consistency (response times within a 0.02s range in the latest run)
2. Maintains slightly better throughput than vLLM (11.14 req/s vs 10.82 req/s)
3. Generates more tokens per second (1151-1158 vs 1074)

These results confirm that the parallelism strategy is crucial for multi-GPU deployments of SGLang, with tensor parallelism providing both better consistency and higher throughput than data parallelism, despite conventional wisdom suggesting data parallelism would be better for throughput with smaller models.

### 4 A10 GPU results

SGLang with tensor parallelism shows more dramatic scaling improvements when moving from 2 to 4 GPUs:

- For 30 concurrent requests: 10.78 req/s → 20.27 req/s (88% improvement)
- For 50 concurrent requests: 17.52 req/s → 24.48 req/s (40% improvement)

vLLM Performance comparison between 2 A10 and 4 A10 GPUs does show some scaling improvements  but the gains are modest.

Refer to the complete result [here](./4A10.md#4.29)

## parameter equivalence discovery

Except for `dp` & `tp` (vllm has `--tensor-parallel-size` but seem no `dp` conterpart) flag confusion, I also had  `--max-total-tokens` misunderstanding, I had thought that was the `--max-model-length` of SGLang.

Early in the testing process, I encountered what appeared to be a dramatic difference in memory usage between the two frameworks:

| Metric       | SGLang              | vLLM                 |
| ------------ | ------------------- | -------------------- |
| Memory Usage | **7,712 MiB (33%)** | **21,058 MiB (91%)** |

This initially led me to believe that SGLang had extraordinary memory efficiency compared to vLLM. However, after further investigation, I discovered this was due to a misunderstanding of parameter equivalence between the frameworks.

### What Happened

When launching SGLang, I used:

```
python3 -m sglang.launch_server --model-path /home/vllm/llm/Qwen7B-awq --max-total-tokens 8192
```

While for vLLM, I used:

```
vllm serve /home/vllm/llm/Qwen7B-awq --max-model-len 8192
```

The key insight: `--max-total-tokens` in SGLang is **not** equivalent to `--max-model-len` in vLLM. The proper equivalent parameter is `--context-length`.

### The Correction

After correcting the parameter to `--context-length` in SGLang, the memory usage became comparable between the frameworks. This experience highlights:

1. The importance of understanding parameter equivalence when benchmarking different frameworks
2. How seemingly minor configuration differences can dramatically impact resource utilization
3. The necessity of careful parameter selection when deploying these frameworks in production

This misunderstanding initially led to incorrect conclusions about memory efficiency, but ultimately provided valuable insight into how these frameworks allocate resources differently. It's a reminder that proper configuration is as important as the framework choice itself.

## Performance Analysis

### SGLang Performance Analysis

Using tensor parallelism (`--tp`) instead of data parallelism (`--dp`) in multi-GPU configuration, SGLang demonstrated several impressive performance characteristics:

1. **Extremely consistent response times** - The standard deviation was only 0.01 seconds, with virtually no difference between min (1.51s) and max (1.52s) response times. This consistency is rare in LLM inference.
2. **High token generation speed** - 333 tokens per second for low concurrency and up to 1544 tokens per second at higher concurrency
3. **Very low latency** - Average response times of 1.51 seconds for generating ~100 tokens per request
4. **Efficient batch processing** - Effective handling of concurrent requests in a single GPU
5. **Warm-up Effect** - The first run has more variable response times, after warm-up, consistency improves dramatically. Check the next section for detailed analysis.

### vLLM Performance Analysis

vLLM shows a few distinguishing characteristics compared to SGLang in our testing:

In both single and multi-GPU setups:

1. **No Warm-up needed**: SGLang showed a significant "warm-up effect" requiring initial requests to reach optimal performance, while vLLM delivered consistent performance from the first request without warm-up.
2. **Lower minimum response time** - Consistently showed lower minimum response times (0.78-1.36s) compared to SGLang's minimum times (1.51-2.68s)
3. **More mature ecosystem** - As a more established project with a longer history, vLLM likely offers greater stability and a broader range of deployment options
4. **Higher variability** - Standard deviation of 0.14-0.28s compared to SGLang TP's extremely tight 0.01-0.03s
5. **Potentially unexplored optimizations** - Our tests used default configurations, and vLLM may benefit from further fine-tuning of parameters for this specific workload

It's worth noting that vLLM is widely adopted in production environments and has undergone extensive real-world testing across various deployment scenarios. While our specific test configuration showed SGLang with tensor parallelism outperforming vLLM in consistency and throughput, vLLM's maturity and active development may offer advantages not captured in these benchmarks.

This performance analysis represents a snapshot of current capabilities with our specific hardware, model, and configuration choices.

## Warm-up Effect

SGLang exhibits a "warm-up" effect:

### SGLang Performance: First Run vs. Warmed Up (5 concurrent requests)

| Metric                | First Run (Cold) | Warmed Up  |
| --------------------- | ---------------- | ---------- |
| Average Response Time | 1.63s            | 1.51s      |
| Standard Deviation    | 0.22s            | 0.01s      |
| Throughput            | 3.06 req/s       | 3.31 req/s |

1. The first run has more variable response times (std dev 0.22s)
2. After warm-up, consistency improves dramatically (std dev 0.01s)
3. Throughput increases slightly after warm-up

This behavior is common in systems using JIT compilation or optimization techniques. The system seems to optimize based on the observed workload patterns.

In a fair comparison with vLLM (which showed std dev of 0.25s), SGLang's first run is quite comparable in terms of consistency. However, after warm-up, SGLang pulls significantly ahead in single-GPU deployments.

For production deployments, this suggests:

1. You might want to "prime" SGLang with some initial requests before sending production traffic
2. The consistency advantage becomes pronounced in long-running single-GPU services
3. Both systems show similar cold-start behavior, but SGLang optimizes more effectively over time on single GPUs

## Limitations and Suggestions

### Potential Limitations

1. **Test duration**: Short tests may not capture long-running behavior or memory leaks
2. **Multi-turn conversations**: the tests only do single-turn conversation while SGLang's RadixAttention is said to be excel at multi-turn conversations.
3. **Prompt diversity**: Using similar/identical prompts might not represent varied real-world workloads
4. **Configuration optimization**: Each framework might benefit from different configuration parameters
5. **Output token variability**: If the number of generated tokens varies between tests, it can affect timing
6. **Limited model architectures**: Results might vary with different model architectures or sizes
7. **Lack of error handling testing**: How systems perform under error conditions wasn't evaluated

### Suggestions for More Comprehensive Testing

1. **Longer duration tests**: Run longer tests (hours) to check for memory stability
2. **Varied prompt lengths**: Test with short, medium, and long prompts
3. **Different model sizes**: Try multiple model sizes if available
4. **Stress testing to failure**: Find breaking points for each system
5. **Measure cold start times**: If relevant for your use case
6. **Test with real application patterns**: Use actual request patterns from your application

## Testing Scripts

This repository includes the scripts used for testing:
- `sglang_stress_test.py`: Script for testing SGLang
- `vllm_stress_test.py`: Script for testing vLLM

These scripts measure key performance metrics including response times, throughput, token generation rate, and more. They are provided as-is and contributions to improve them are welcome.

## Running Your Own Tests

To reproduce these tests or run your own variants:

```bash
# Install requirements
pip install -r requirements.txt

# Test SGLang
python sglang_stress_test.py --url "http://localhost:30000/generate" --concurrent 30 --total 300

# Test vLLM
python vllm_stress_test.py --url "http://localhost:8000/v1/completions" --model "your-model" --concurrent 30 --total 300
```

Modify the parameters to match your setup and requirements.

## Important Notes on Performance Testing

Performance testing can be insightful but is rarely definitive. Before reviewing these results, please consider these common limitations in benchmarking:

- **Test conditions matter**: Results are specific to the hardware, model, and configuration used
- **Your mileage may vary**: Different workloads may produce significantly different results
- **Snapshot in time**: Both frameworks are actively developed, so performance characteristics may change
- **Optimization potential**: Neither framework may be fully optimized for this specific workload
- **Limited scope**: These tests focus on specific metrics and may not capture all relevant performance dimensions
- **Short-duration effects**: Brief tests might not capture long-term behavior like memory leaks or throttling

This testing aims to provide a reasonable comparison under specific conditions, not a definitive judgment on which framework is "better" in all cases.

## ~~Conclusion~~

Please check appendix section for the overall conclusion.

### Short Version

Beware of the initial warm-up phase and a potentially steeper learning curve; however, for maximizing sustained performance, our benchmarks indicate SGLang is generally the more advantageous choice over vLLM once appropriately configured and warmed up.

### Long Version

The performance comparison between SGLang and vLLM yielded nuanced results that highlight important considerations for LLM deployment beyond simple throughput numbers. 

Key takeaways include:

#### Performance Characteristics

1. **SGLang excelled with tensor parallelism**: Showed extremely consistent response times and excellent throughput in both single and multi-GPU configurations when properly configured with `--tp`.

2. **Configuration dramatically impacted performance**: SGLang with data parallelism performed significantly worse than with tensor parallelism, highlighting how critical parallelism strategy choice is.
3. **Warm-up differences**: SGLang showed a significant "warm-up effect" requiring initial requests to reach optimal performance, while vLLM delivered consistent performance from the first request without warm-up.

4. **vLLM provided lower minimum latency**: While not matching SGLang's consistency with tensor parallelism, vLLM consistently delivered lower minimum response times across all test scenarios.

5. **Scaling efficiency differences**: SGLang with tensor parallelism showed substantially better scaling when moving from 2 to 4 GPUs (up to 88% throughput improvement) compared to vLLM (only 15-20% improvement in most scenarios). This suggests SGLang may have better scaling characteristics for deployments with higher GPU counts.

#### Critical Configuration Discoveries

1. **Parallelism strategy matters enormously**: For SGLang, using tensor parallelism (`--tp`) instead of data parallelism (`--dp`) in multi-GPU setups dramatically improved performance, changing it from significantly worse than vLLM to significantly better.
2. **Parameter equivalence is critical**: Proper configuration of equivalent parameters across frameworks (`--max-model-len` in vLLM vs. `--context-length` in SGLang) is essential for fair comparisons and optimal resource utilization.

#### Key Takeaways for Deployment

These findings suggest that:

1. **Framework choice matters**: Different frameworks have different optimal use cases
2. **Configuration details are critical**: Small changes in configuration can dramatically impact performance
3. **Test your specific deployment scenario**: Results may vary significantly based on hardware, model, and parallelism strategy

Most importantly, the impact of parallelism strategy on SGLang highlights that commonly accepted guidelines about when to use tensor vs. data parallelism may need reconsideration. For workloads where response time consistency is a priority, tensor parallelism may be superior even for models that easily fit on a single GPU.

I encourage users to run their own tests with workloads representative of their actual production needs and hardware configurations, and to experiment with different parallelism strategies rather than following general guidelines without testing.



## Appendix: Qwen3-4B

### Executive Summary

"Qwen3 models will think before respond." Both frameworks were launched using standard commands without reasoning-specific parameters, the thinking mode was controlled through request parameters (`enable_thinking: true/false`)  

- **SGLang** `python -m sglang.launch_server --model-path Qwen/Qwen3-4B`
- **vLLM**: `vllm serve Qwen/Qwen3-4B` 

In my initial test, both SGLang and vLLM showed excellent consistent response times for both native api and OpenAI-compatible APIs. 

1. **Native APIs**: SGLang's `/generate` endpoint vs vLLM's `/v1/completions`
2. **OpenAI-compatible APIs**: Both frameworks' `/v1` endpoints for direct comparison

What was even more confusing was that **turning on** think mode would get better response times. Then I figured out why! I had set `max_tokens` to 256, so almost all responses were truncated with `finish_reason='length'`. For think mode, since the response contains `"<think>..."` formatting, it reached the 256 token limit faster, resulting in even more consistent (but artificially shortened) responses.

For completest test result for `max_tokens=256`, please refer to [here](./qwen3-256.md)

To make fair comparisons, I tested different `max_tokens` values for both OpenAI APIs and Native APIs, leading to a discovery about parameter compliance differences: both SGlang and vLLM‘s `openai` APIs respect `max_tokens` parameter. SGLang's native api **completely ignores max_tokens parameter** while vLLM's native api generates **exactly** the `max_tokens` amount of tokens.

### Performance Analysis

For completest test result, please refer to [here](./qwen3-final.md)

#### OpenAI API Performance (10 concurrent, 100 requests)

**With Thinking Mode (max_tokens=3096)**

| Metric                    | vLLM              | SGLang          | Winner   |
| ------------------------- | ----------------- | --------------- | -------- |
| **Average Response Time** | **16.64-17.54s**  | 18.59-19.10s    | **vLLM** |
| **Standard Deviation**    | **6.53-6.91s**    | 6.84-7.64s      | **vLLM** |
| **Actual Throughput**     | **0.39 req/s**    | 0.36-0.38 req/s | **vLLM** |
| **Tokens Per Second**     | **377-395 tok/s** | 337-369 tok/s   | **vLLM** |

**Without Thinking Mode (max_tokens=3096)**

| Metric                    | vLLM                | SGLang          | Winner   |
| ------------------------- | ------------------- | --------------- | -------- |
| **Average Response Time** | **6.0-7.0s**        | 7.8-8.9s        | **vLLM** |
| **Standard Deviation**    | **4.4-4.7s**        | 5.6-6.2s        | **vLLM** |
| **Actual Throughput**     | **0.66-0.70 req/s** | 0.57-0.59 req/s | **vLLM** |

**Controlled Token Length (max_tokens=512, no thinking)**

| Metric                    | vLLM                | SGLang          | Winner   |
| ------------------------- | ------------------- | --------------- | -------- |
| **Average Response Time** | **4.1-4.7s**        | 4.6-5.2s        | **vLLM** |
| **Actual Throughput**     | **1.71-1.75 req/s** | 1.56-1.64 req/s | **vLLM** |
| **Tokens Per Second**     | **434-470 tok/s**   | 401-414 tok/s   | **vLLM** |

#### Native api

**SGlang**: **Completely ignores max_tokens parameter**

- max_tokens=512 → generates ~128 tokens (actual: 101-128 range)
- max_tokens=1024 → generates ~128 tokens (actual: 101-128 range)
- max_tokens=3096 → generates ~128 tokens
- **All responses show `completion_tokens: 128` and `finish_reason: {'type': 'length', 'length': 128}`**

**vLLM API**: Respects max_tokens parameter precisely

- max_tokens=512 → generates exactly 512 tokens
- max_tokens=1024 → generates exactly 1024 tokens  

- **Response time scales predictably with token count**

So comparisons between them become **pointless**.

## Quick Recommendation 

**For most use cases, choose vLLM.**  vLLM provides better performance for Qwen3-4B in my test and consistent performance across models and APIs - Better OpenAI compatibility (required for most production deployments)   - More mature ecosystem and broader adoption - Lower configuration complexity 

Unless you have very specific requirements and can thoroughly test both frameworks with your exact setup, vLLM is the safer, more reliable choice.

## Contributing

Contributions to improve the testing methodology or scripts are welcome! Please open an issue or PR with your suggestions.

## License

**Creative Commons** (**CC**) **license**
