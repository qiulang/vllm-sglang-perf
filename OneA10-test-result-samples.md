## Sglang 和 vllm 性能测试比较

### sglang

```
// 第一次启动时间

Test completed in 6.53 seconds
        SGLang Stress Test Results - 2025-04-25 21:27:40        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 5                               │
│ Total Requests             │ 20                              │
│ Successful Requests        │ 20 (100.0%)                     │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 6.53 seconds                    │
│ Min Response Time          │ 1.50 seconds                    │
│ Max Response Time          │ 2.01 seconds                    │
│ Average Response Time      │ 1.63 seconds                    │
│ Median Response Time       │ 1.51 seconds                    │
│ P90 Response Time          │ 2.01 seconds                    │
│ P95 Response Time          │ 2.01 seconds                    │
│ P99 Response Time          │ 2.01 seconds                    │
│ Std Dev Response Time      │ 0.22 seconds                    │
│ Theoretical Max Throughput │ 9.96 requests/second            │
│ Actual Throughput          │ 3.06 requests/second            │
│ Total Generated Tokens     │ 2043                            │
│ Tokens Per Second          │ 313.00                          │
│ Avg Tokens Per Request     │ 102.15                          │
│ Peak Requests In Flight    │ 5                               │
└────────────────────────────┴─────────────────────────────────┘

// 之后两次完全一致
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

Test completed in 6.05 seconds
        SGLang Stress Test Results - 2025-04-25 21:28:09        
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
│ Theoretical Max Throughput │ 13.15 requests/second           │
│ Actual Throughput          │ 3.31 requests/second            │
│ Total Generated Tokens     │ 2064                            │
│ Tokens Per Second          │ 341.08                          │
│ Avg Tokens Per Request     │ 103.20                          │
│ Peak Requests In Flight    │ 5                               │
└────────────────────────────┴─────────────────────────────────┘

//加量测试
Test completed in 20.11 seconds
        SGLang Stress Test Results - 2025-04-25 21:46:46        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 20.11 seconds                   │
│ Min Response Time          │ 1.98 seconds                    │
│ Max Response Time          │ 2.15 seconds                    │
│ Average Response Time      │ 2.01 seconds                    │
│ Median Response Time       │ 1.99 seconds                    │
│ P90 Response Time          │ 2.15 seconds                    │
│ P95 Response Time          │ 2.15 seconds                    │
│ P99 Response Time          │ 2.15 seconds                    │
│ Std Dev Response Time      │ 0.05 seconds                    │
│ Theoretical Max Throughput │ 139.34 requests/second          │
│ Actual Throughput          │ 14.92 requests/second           │
│ Total Generated Tokens     │ 31071                           │
│ Tokens Per Second          │ 1544.94                         │
│ Avg Tokens Per Request     │ 103.57                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 20.05 seconds
        SGLang Stress Test Results - 2025-04-25 22:02:22        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 20.05 seconds                   │
│ Min Response Time          │ 1.91 seconds                    │
│ Max Response Time          │ 2.01 seconds                    │
│ Average Response Time      │ 2.00 seconds                    │
│ Median Response Time       │ 2.00 seconds                    │
│ P90 Response Time          │ 2.01 seconds                    │
│ P95 Response Time          │ 2.01 seconds                    │
│ P99 Response Time          │ 2.01 seconds                    │
│ Std Dev Response Time      │ 0.01 seconds                    │
│ Theoretical Max Throughput │ 148.98 requests/second          │
│ Actual Throughput          │ 14.96 requests/second           │
│ Total Generated Tokens     │ 31148                           │
│ Tokens Per Second          │ 1553.38                         │
│ Avg Tokens Per Request     │ 103.83                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

/******  When I wrongly set `--max-total-tokens` instead of `context-length` ******/
/****** I was surprised sglang only used 7G memory  *****/

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

### vllm

```
// 第一次启动时间
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

est completed in 8.70 seconds
           vLLM Stress Test Results - 2025-04-25 22:10:24            
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
│ Total Test Duration        │ 8.70 seconds                         │
│ Min Response Time          │ 1.31 seconds                         │
│ Max Response Time          │ 2.63 seconds                         │
│ Average Response Time      │ 1.67 seconds                         │
│ Median Response Time       │ 1.56 seconds                         │
│ P90 Response Time          │ 2.25 seconds                         │
│ P95 Response Time          │ 2.63 seconds                         │
│ P99 Response Time          │ 2.63 seconds                         │
│ Std Dev Response Time      │ 0.35 seconds                         │
│ Theoretical Max Throughput │ 7.60 requests/second                 │
│ Actual Throughput          │ 2.30 requests/second                 │
│ Total Generated Tokens     │ 2013                                 │
│ Tokens Per Second          │ 231.51                               │
│ Avg Tokens Per Request     │ 100.65                               │
│ Peak Requests In Flight    │ 5                                    │
└────────────────────────────┴──────────────────────────────────────┘

Test completed in 7.61 seconds
           vLLM Stress Test Results - 2025-04-25 22:11:33            
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
│ Total Test Duration        │ 7.61 seconds                         │
│ Min Response Time          │ 1.22 seconds                         │
│ Max Response Time          │ 1.99 seconds                         │
│ Average Response Time      │ 1.65 seconds                         │
│ Median Response Time       │ 1.71 seconds                         │
│ P90 Response Time          │ 1.95 seconds                         │
│ P95 Response Time          │ 1.99 seconds                         │
│ P99 Response Time          │ 1.99 seconds                         │
│ Std Dev Response Time      │ 0.24 seconds                         │
│ Theoretical Max Throughput │ 10.06 requests/second                │
│ Actual Throughput          │ 2.63 requests/second                 │
│ Total Generated Tokens     │ 1977                                 │
│ Tokens Per Second          │ 259.66                               │
│ Avg Tokens Per Request     │ 98.85                                │
│ Peak Requests In Flight    │ 5                                    │
└────────────────────────────┴──────────────────────────────────────┘

Test completed in 34.94 seconds
           vLLM Stress Test Results - 2025-04-25 21:36:22            
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
│ Total Test Duration        │ 34.94 seconds                        │
│ Min Response Time          │ 1.40 seconds                         │
│ Max Response Time          │ 4.38 seconds                         │
│ Average Response Time      │ 2.57 seconds                         │
│ Median Response Time       │ 2.55 seconds                         │
│ P90 Response Time          │ 2.93 seconds                         │
│ P95 Response Time          │ 3.04 seconds                         │
│ P99 Response Time          │ 4.35 seconds                         │
│ Std Dev Response Time      │ 0.36 seconds                         │
│ Theoretical Max Throughput │ 68.50 requests/second                │
│ Actual Throughput          │ 8.59 requests/second                 │
│ Total Generated Tokens     │ 30464                                │
│ Tokens Per Second          │ 871.90                               │
│ Avg Tokens Per Request     │ 101.55                               │
│ Peak Requests In Flight    │ 30                                   │
└────────────────────────────┴──────────────────────────────────────┘

Test completed in 31.56 seconds
           vLLM Stress Test Results - 2025-04-25 21:36:57            
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
│ Total Test Duration        │ 31.56 seconds                        │
│ Min Response Time          │ 1.40 seconds                         │
│ Max Response Time          │ 3.51 seconds                         │
│ Average Response Time      │ 2.57 seconds                         │
│ Median Response Time       │ 2.57 seconds                         │
│ P90 Response Time          │ 2.95 seconds                         │
│ P95 Response Time          │ 3.01 seconds                         │
│ P99 Response Time          │ 3.19 seconds                         │
│ Std Dev Response Time      │ 0.30 seconds                         │
│ Theoretical Max Throughput │ 85.40 requests/second                │
│ Actual Throughput          │ 9.50 requests/second                 │
│ Total Generated Tokens     │ 30335                                │
│ Tokens Per Second          │ 961.05                               │
│ Avg Tokens Per Request     │ 101.12                               │
│ Peak Requests In Flight    │ 30                                   │
└────────────────────────────┴──────────────────────────────────────┘



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

