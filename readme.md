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
- [Contributing](#contributing)
- [License](#license)

## Introduction

SGLang and vLLM are both high-performance inference frameworks for large language models, with SGLang taking a compilation-based approach while vLLM focuses on optimized attention and memory management.

Before starting this comparison, I had no bias toward either framework and was simply curious about their relative performance. The results turned out to be quite surprising and nuanced, with each framework showing distinct advantages in different deployment scenarios.

Benchmark testing without clear objectives can often be misleading and produce non-objective results. However, this project has a specific, focused goal: to evaluate how vLLM and SGLang perform when running a small LLM model on a **mid-range** NVIDIA GPU like A10, in both single and multi-GPU configurations.

For this test, I selected the Qwen 2.5 7B quantized model. I specifically chose its AWQ variant rather than the GPTQ int 4-bit model, based on both information from sources like https://github.com/mit-han-lab/llm-awq and my own testing, which showed AWQ outperforming GPTQ int 4-bit models.

This represents a practical, real-world scenario for organizations deploying smaller quantized models on accessible hardware, rather than focusing on high-end multi-GPU setups that may be less common in production environments.

## Test Setup

### Hardware
- Single and dual [NVIDIA A10 GPU (24GB)](https://www.nvidia.com/en-us/data-center/products/a10-gpu/) configurations
- Intel® Xeon® Gold 6326 Processor, **30** GiB memory

### Software
- Ubuntu 22, GPU Driver 550.127.08/CUDA 12.4.1/CUDNN 9.2.0.82
- Conda 23.7.4, python 3.12
- SGLang (version 0.4.5 latest, `pip install "sglang[all]>=0.4.5.post3"` )
- vLLM (version v0.8.4 latest, `pip install vllm`)
- Model: [Qwen2.5 7B-AWQ (quantized)](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ)

### Test Parameters
- Requests: 20 (small test) and 300 (larger test)
- Concurrency: 5 and 30 concurrent requests
- Identical prompts with max_tokens=256

### Test workflow

1. Setup:
   - Started with a clean Ubuntu 22 machine with only CUDA & Conda environments installed
   - No other GPU processes running during tests as nvidia-smi shows zero usage.

2. First SGLang testing:
   - Start the SGLang server, `python3 -m sglang.launch_server --model-path $MODEL_PATH --context-length 8192 --dp 1 or 2`
   - Run the SGLang stress test script (which is provided as-is and may benefit from further refinement)
   - Record the performance metrics

3. For vLLM testing:
   - Stop the SGLang server
   - Start the vLLM server, `vllm serve $MODEL_PATH --max-model-len 8192 --tensor-parallel-size 1 or 2`
   - Run the vLLM stress test script
   - Record the performance metrics

4. Repeat for both single and dual GPU configurations

## Key Findings

### The most striking finding

The most striking discovery from this testing is the dramatic reversal in performance characteristics between single-GPU and multi-GPU configurations:

1. **In single-GPU scenarios**: SGLang demonstrated extremely consistent response times, higher throughput, and comparable memory usage when properly configured.

2. **In multi-GPU scenarios**: vLLM maintained consistent performance while SGLang showed significant variability and decreased throughput.

3. **Unexpected scaling behavior for SGLang** : When testing SGLang on 2 A10 GPUs compared to a single A10 GPU, performance surprisingly **degraded rather than improved**. With 2 GPUs, SGLang showed significantly higher response time variance (std dev increasing from 0.01s to 1.94-2.37s) and less predictable throughput (for 5 & 30 concyrrent requests). This counter-intuitive finding suggests that SGLang may be optimized for single-GPU performance, and its current implementation might not efficiently distribute work across multiple GPUs.  Refer to the test result [here](./TwoA10-test-result-samples.md)

## Single-GPU Results

### Memory Usage (with correct parameter configuration)

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

When testing with 2 A10 GPUs, the performance characteristics reversed dramatically:

### Multi-GPU Test Results

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
└────────────────────────────┴─────────────────────────────────┘
```

**For 2 A10 GPU, SGLang showed significantly higher response time variance and less predictable throughput.** At the first it is hard to believe this, so I test many times to confirmed that.

For 2 A10 GPU, vLLM indeed showed a slightly better result for 1 A10 GPU.


#### vLLM with 30 Concurrent Requests (300 total)

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

#### Another vLLM run showing similar consistency:

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

### Multi-GPU Comparison

| Metric                | SGLang (Run 1) | SGLang (Run 2) | vLLM (Run 1) | vLLM (Run 2) |
|-----------------------|----------------|----------------|--------------|--------------|
| Min Response Time     | 1.55s          | 1.52s          | 1.34s        | 1.23s        |
| Max Response Time     | 8.58s          | 12.37s         | 2.97s        | 3.62s        |
| Average Response Time | 3.23s          | 4.44s          | 2.26s        | 2.32s        |
| Std Dev Response Time | 1.94s          | 2.37s          | 0.27s        | 0.28s        |
| Actual Throughput     | 8.13 req/s     | 4.92 req/s     | 10.82 req/s  | 10.09 req/s  |
| Tokens Per Second     | 853.94         | 511.92         | 1074.01      | 1025.81      |

Refer to the complete result [here](./TwoA10-test-result-samples.md)

## The `--max-total-tokens` Misunderstanding

Early in the testing process, I encountered what appeared to be a dramatic difference in memory usage between the two frameworks:

| Metric       | SGLang              | vLLM                 |
| ------------ | ------------------- | -------------------- |
| Memory Usage | **7,712 MiB (33%)** | **21,058 MiB (91%)** |

This initially led me to believe that SGLang had extraordinary memory efficiency compared to vLLM. However, after further investigation, I discovered this was due to a misunderstanding of parameter equivalence between the frameworks.

### What Happened

When launching SGLang, I used:

```
python3 -m sglang.launch_server --model-path /home/vllm/llm/Qwen7B-awq/ --max-total-tokens 8192
```

While for vLLM, I used:

```
vllm serve qwen7B-awq --port 8000 --max-model-len 8192
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

In the single-GPU configuration, SGLang demonstrated several impressive performance characteristics:

1. **Extremely consistent response times** - The standard deviation was only 0.01 seconds, with virtually no difference between min (1.51s) and max (1.52s) response times. This consistency is rare in LLM inference.
2. **High token generation speed** - 333 tokens per second for low concurrency and up to 1544 tokens per second at higher concurrency
3. **Very low latency** - Average response times of 1.51 seconds for generating ~100 tokens per request
4. **Efficient batch processing** - Effective handling of concurrent requests in a single GPU

However, in multi-GPU setups, SGLang showed significant performance degradation:

1. **Highly variable response times** - Standard deviation increased to 1.94-2.37 seconds
2. **Wide latency range** - Response times varied from as low as 1.52s to as high as 12.37s
3. **Reduced throughput** - Both absolute throughput and scaling efficiency declined
4. **Unpredictable performance** - Large variance between test runs

### vLLM Performance Analysis

vLLM showed different strengths depending on the deployment configuration:

In single-GPU setups:
1. **Good but not exceptional response times** - Average of 1.64-2.57 seconds
2. **Moderate consistency** - Standard deviation of 0.20-0.30 seconds
3. **Solid throughput** - 2.65-9.50 requests per second depending on concurrency

vLLM truly shined in multi-GPU setups:
1. **Consistent response times** - Maintained low standard deviation (0.27-0.28 seconds)
2. **Predictable latency range** - Tight band between min and max response times
3. **Higher throughput** - Outperformed SGLang in actual requests per second
4. **Stable performance** - Consistent results across multiple test runs

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
2. **Prompt diversity**: Using similar/identical prompts might not represent varied real-world workloads
3. **Configuration optimization**: Each framework might benefit from different configuration parameters
4. **Output token variability**: If the number of generated tokens varies between tests, it can affect timing
5. **Limited model architectures**: Results might vary with different model architectures or sizes
6. **Lack of error handling testing**: How systems perform under error conditions wasn't evaluated

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

## Conclusion

The performance comparison between SGLang and vLLM yielded surprising and nuanced results that highlight how scaling affects these frameworks differently:

### Single-GPU Performance (A10)
In the single A10 GPU scenario, SGLang demonstrated remarkable advantages:
- **Response consistency**: Extremely consistent response times (std dev of just 0.01s)
- **Throughput**: ~57% higher throughput than vLLM
- **Token generation**: Faster token generation rate

### Multi-GPU Performance (2x A10)
When testing with 2 A10 GPUs, the performance characteristics reversed dramatically:
- **Response consistency**: vLLM maintained consistent response times (std dev of 0.27s), while SGLang showed extreme variability (std dev up to 2.37s)
- **Response time range**: vLLM maintained a tight range (1.34s-2.97s) compared to SGLang's dramatic spread (as wide as 1.52s-12.37s in some tests)
- **Throughput**: vLLM achieved more than double the throughput in worst cases (10.82 req/s vs as low as 4.92 req/s for SGLang)
- **Predictability**: vLLM offered much more predictable performance at scale, critical for production systems

### Key Insights
These findings suggest that:
1. **Framework strengths vary by scale**: The two frameworks optimize differently for single vs. multi-GPU deployments
2. **Deployment architecture matters**: Your hardware configuration should strongly influence your framework choice
3. **No one-size-fits-all solution**: Each framework has scenarios where it excels

One of the most valuable questions for the community to explore is: **Why does SGLang's performance consistency degrade in multi-GPU settings while vLLM maintains or improves its consistency?** Understanding these scaling behaviors could provide important insights for both framework developers and users.

The optimal choice between frameworks clearly depends on your specific use case, hardware configuration, and requirements. For single-GPU deployments, SGLang's consistency and efficiency are compelling. For multi-GPU setups, vLLM appears to maintain better scaling characteristics.

I encourage users to run their own tests with workloads representative of their actual production needs and hardware configurations.

## Contributing

Contributions to improve the testing methodology or scripts are welcome! Please open an issue or PR with your suggestions.

## License

**Creative Commons** (**CC**) **license**
