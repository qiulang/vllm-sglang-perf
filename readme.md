# SGLang vs vLLM Performance Comparison (sort of)

## Introduction

Benchmark testing without clear objectives can often be misleading and produce non-objective results. However, this project has a specific, focused goal: to evaluate how vLLM and SGLang perform when running a small LLM model on a **mid-range** NVIDIA GPU like A10. 

For this test, I selected the Qwen 2.5 7B quantized model. I specifically chose its AWQ variant rather than the GPTQ int 4-bit model, based on both information from sources like https://github.com/mit-han-lab/llm-awq and my own testing, which showed AWQ outperforming GPTQ int 4-bit models.

This represents a practical, real-world scenario for organizations deploying smaller quantized models on accessible hardware, rather than focusing on high-end multi-GPU setups that may be less common in production environments.

**Before the test I have no idea what result I will get as I have no bias for either of them, but the result turns out to be quite surpring.**


## Test Setup

### Hardware
- [NVIDIA A10 GPU (24GB)](https://www.nvidia.com/en-us/data-center/products/a10-gpu/)
- Intel® Xeon® Gold 6326 Processor,  **30** GiB memory

### Software
- Ubuntu 22, conda 23.7.4, python 3.12
- SGLang (version 0.4.5 latest)
- vLLM (version v0.8.4 latest)
- Model: [Qwen2.5 7B-AWQ (quantized) ](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ)

### Test Parameters
- Requests: 20 (small test) and 300 (larger test)
- Concurrency: 5 and 30 concurrent requests
- Identical prompts with max_tokens=256

### Test workflow

1. First SGLang testing:
   - Start the SGLang server
   - Run the SGLang stress test script (my gloriously unrefined code, lol)
   - Record the performance metrics
2. For vLLM testing:
   - Stop the SGLang server
   - Start the vLLM server
   - Run the vLLM stress test script (my gloriously unrefined code, lol)
   - Record the performance metrics

## Key Findings

### The most striking finding

The most striking finding is from the GPU usage report when SGLang delivers higher throughput than vLLM, more consistent response times, similar or better token generation rates

| Metric                     | SGLang              | vLLM                 |
| -------------------------- | ------------------- | -------------------- |
| Memory Usage               | **7,712 MiB (33%)** | **21,058 MiB (91%)** |
| GPU Utilization            | 92%                 | 93%                  |
| Power Consumption          | 151W                | 145W                 |
| Temperature                | 49°C                | 50°C                 |
| Throughput (30 concurrent) | 14.92 req/s         | 9.50 req/s           |

The patterns are remarkably consistent:

1. **Similar GPU computational intensity**: Both frameworks use around 92-93% of the GPU's compute capacity
2. **Dramatically different memory efficiency**: SGLang uses less than half the memory of vLLM
3. **Similar power profiles**: Both use around 145-151W

What makes this particularly impressive is that SGLang is delivering about **57% higher** throughput while using **63% less memory**. The computational efficiency difference is substantial.

 `nvidai-smi` result sample for **SGLang** 

```
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      8715      C   sglang::scheduler_TP0                        7706MiB |
+-----------------------------------------------------------------------------------------+
Fri Apr 25 22:21:23 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.127.08             Driver Version: 550.127.08     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A10                     On  |   00000000:00:07.0 Off |                    0 |
|  0%   49C    P0            148W /  150W |    7712MiB /  23028MiB |     91%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

 `nvidai-smi` result sample for **vllm** 

```
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      8371      C   ...iniconda3/envs/vllm_env/bin/python3      21052MiB |
+-----------------------------------------------------------------------------------------+
Fri Apr 25 22:19:31 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.127.08             Driver Version: 550.127.08     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A10                     On  |   00000000:00:07.0 Off |                    0 |
|  0%   50C    P0            153W /  150W |   21058MiB /  23028MiB |     95%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

### Performance Metrics
- **Memory Usage**: SGLang used ~33% of GPU memory vs. vLLM's ~91% for the same model
- **Response Time**: SGLang demonstrated more **consistent** response times (lower standard deviation)
- **Throughput**: At 30 concurrent requests, SGLang achieved ~57% higher throughput
- **GPU Utilization**: Both frameworks utilized the GPU efficiently (91-95%)

### Test result sample 

SGlang  for 5 Concurrent Requests (20 total)

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

vLLM  for 5 Concurrent Requests (20 total)

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


### Detailed Results

#### 5 Concurrent Requests (20 total)
| Metric | SGLang | vLLM |
|--------|--------|------|
| Avg Response Time | 1.51s | 1.72s |
| Std Dev | 0.01s | 0.25s |
| Throughput | 3.31 req/s | 2.46 req/s |
| Memory Usage | 7.7 GB | 21.1 GB |

#### 30 Concurrent Requests (300 total)
| Metric | SGLang | vLLM |
|--------|--------|------|
| Avg Response Time | 2.01s | 2.57s |
| Std Dev | 0.05s | 0.30s |
| Throughput | 14.92 req/s | 9.50 req/s |
| Token Generation | 1544.94 tok/s | 961.05 tok/s |



### SGLang results summary

The SGLang results shows several impressive performance characteristics:

1. **Extremely consistent response times** - The standard deviation is only 0.01 seconds, and there's virtually no difference between min (1.51s) and max (1.52s) response times. This is remarkable consistency that's very rare in LLM inference.
2. **High token generation speed** - 341.08 tokens per second overall is excellent for a 7B parameter model, especially if it's running on a single GPU.
3. **Very low latency** - The average response time of 1.51 seconds for generating ~103 tokens per request is quite fast.
4. **Efficient batch processing** - The fact that the actual throughput (3.31 req/s) is significantly higher than what you'd expect from the response time alone suggests that SGLang is efficiently batching these requests.

This combination is quite remarkable and suggests SGLang is using sophisticated compilation techniques to optimize the inference process. The dramatically lower memory footprint with similar computational intensity points to:

1. Better memory layout and access patterns
2. More efficient kernel implementations
3. Possibly specialized optimizations for this particular model architecture

For production deployments, SGLang's memory efficiency would allow you to:

- Run larger batch sizes
- Handle more concurrent users
- Potentially fit larger models in the same GPU
- Run multiple model instances on a single GPU

These characteristics make SGLang particularly attractive for high-throughput production environments where GPU memory is often the limiting factor.

## "warm-up" effect

Compared vllm, SGlang exhibits a "warm-up" effect where:

### SGLang Performance: First Run vs. Warmed Up (5 concurrent requests)

| Metric                | First Run (Cold) | Warmed Up  |
| --------------------- | ---------------- | ---------- |
| Average Response Time | 1.63s            | 1.51s      |
| Standard Deviation    | 0.22s            | 0.01s      |
| Throughput            | 3.06 req/s       | 3.31 req/s |

1. The first run has more variable response times (std dev 0.22s)
2. After warm-up, consistency improves dramatically (std dev 0.01s)
3. Throughput increases slightly after warm-up

This behavior is actually common in many ML inference systems, including those using JIT compilation or optimization techniques. The system seems to optimize based on the observed workload patterns.

In a fair comparison with vLLM (which showed std dev of 0.25s), SGLang's first run is actually quite comparable in terms of consistency. However, after warm-up, SGLang pulls significantly ahead.

For production deployments, this suggests:

1. You might want to "prime" SGLang with some initial requests before sending production traffic
2. The consistency advantage becomes even more pronounced in long-running services
3. Both systems show similar cold-start behavior, but SGLang optimizes more effectively over time

This makes SGLang particularly well-suited for persistent services rather than serverless or on-demand deployments where cold starts might be frequent.


## Testing Scripts

This repository includes the scripts used for testing:
- `sglang_stress_test.py`: Script for testing SGLang
- `vllm_stress_test.py`: Script for testing vLLM

### Potential Limitations

1. **Test duration**: Short tests may not capture long-running behavior or memory leaks
2. **Prompt diversity**: Using similar/identical prompts might not represent varied real-world workloads
3. **Configuration optimization**: Each framework might benefit from different configuration parameters
4. **Output token variability**: If the number of generated tokens varies between tests, it can affect timing
5. **Single model architecture**: Results might vary with different model architectures or sizes
6. **Lack of error handling testing**: How systems perform under error conditions wasn't evaluated

### Suggestions for More Comprehensive Testing

1. **Longer duration tests**: Run longer tests (hours) to check for memory stability
2. **Varied prompt lengths**: Test with short, medium, and long prompts
3. **Different model sizes**: Try multiple model sizes if available
4. **Stress testing to failure**: Find breaking points for each system
5. **Measure cold start times**: If relevant for your use case
6. **Test with real application patterns**: Use actual request patterns from your application



**Basically,  please help me refine my test codes** 



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

## ⚠️ Important Notes on Performance Testing

Performance testing can be insightful but is rarely definitive. Before reviewing these results, please consider these common limitations in benchmarking:

- **Test conditions matter**: Results are specific to the hardware, model, and configuration used
- **Your mileage may vary**: Different workloads may produce significantly different results
- **Snapshot in time**: Both frameworks are actively developed, so performance characteristics may change
- **Optimization potential**: Neither framework may be fully optimized for this specific workload
- **Limited scope**: These tests focus on specific metrics and may not capture all relevant performance dimensions
- **Short-duration effects**: Brief tests might not capture long-term behavior like memory leaks or throttling

This testing aims to provide a reasonable comparison under specific conditions, not a definitive judgment on which framework is "better" in all cases.

## Conclusion

SGLang demonstrated significant memory efficiency advantages while delivering higher throughput and more consistent response times for this specific model and test configuration. However, the optimal choice between frameworks depends on your specific use case, hardware, and requirements.

I (Qiulang), encourage users to run their own tests with workloads representative of their actual production needs.

## Contributing

Contributions to improve the testing methodology or scripts are welcome! Please open an issue or PR with your suggestions.

## License

**Creative Commons** (**CC**) **license**
