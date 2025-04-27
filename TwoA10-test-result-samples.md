### SGLang

- `max_prefill_tokens`: Token budget of how many tokens to accept in one prefill batch. The actual number is the max of this parameter and the `context_length`.
- `max_total_tokens`: The maximum number of tokens that can be stored into the KV cache. Use mainly for debugging.
- `context_length`: The number of tokens our model can process *including the input*. Note that extending the default might lead to strange behavior.
- To enable multi-GPU tensor parallelism, add `--tp 2` , To enable multi-GPU data parallelism, add --dp 2. 
- For my small LLM Model test, use --dp 2

https://docs.sglang.ai/backend/server_arguments.html

```
python -m sglang.launch_server --model-path /home/vllm/llm/Qwen7B-awq --context-length 8192 --dp 2


+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A     17126      C   sglang::scheduler_DP0_TP0                   20916MiB |
|    1   N/A  N/A     17127      C   sglang::scheduler_DP1_TP0                   20916MiB |
+-----------------------------------------------------------------------------------------+
Sun Apr 27 14:44:25 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.127.08             Driver Version: 550.127.08     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A10                     On  |   00000000:00:07.0 Off |                    0 |
|  0%   31C    P0             53W /  150W |   20922MiB /  23028MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA A10                     On  |   00000000:00:08.0 Off |                    0 |
|  0%   31C    P0             55W /  150W |   20922MiB /  23028MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+


Test completed in 34.77 seconds
        SGLang Stress Test Results - 2025-04-27 13:26:25        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 34.77 seconds                   │
│ Min Response Time          │ 2.04 seconds                    │
│ Max Response Time          │ 16.34 seconds                   │
│ Average Response Time      │ 3.47 seconds                    │
│ Median Response Time       │ 2.05 seconds                    │
│ P90 Response Time          │ 16.33 seconds                   │
│ P95 Response Time          │ 16.34 seconds                   │
│ P99 Response Time          │ 16.34 seconds                   │
│ Std Dev Response Time      │ 4.29 seconds                    │
│ Theoretical Max Throughput │ 18.36 requests/second           │
│ Actual Throughput          │ 8.63 requests/second            │
│ Total Generated Tokens     │ 31238                           │
│ Tokens Per Second          │ 898.49                          │
│ Avg Tokens Per Request     │ 104.13                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 20.49 seconds
        SGLang Stress Test Results - 2025-04-27 13:27:05        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 20.49 seconds                   │
│ Min Response Time          │ 2.04 seconds                    │
│ Max Response Time          │ 2.05 seconds                    │
│ Average Response Time      │ 2.05 seconds                    │
│ Median Response Time       │ 2.05 seconds                    │
│ P90 Response Time          │ 2.05 seconds                    │
│ P95 Response Time          │ 2.05 seconds                    │
│ P99 Response Time          │ 2.05 seconds                    │
│ Std Dev Response Time      │ 0.00 seconds                    │
│ Theoretical Max Throughput │ 146.27 requests/second          │
│ Actual Throughput          │ 14.64 requests/second           │
│ Total Generated Tokens     │ 31255                           │
│ Tokens Per Second          │ 1525.57                         │
│ Avg Tokens Per Request     │ 104.18                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 20.45 seconds
        SGLang Stress Test Results - 2025-04-27 13:28:14        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 20.45 seconds                   │
│ Min Response Time          │ 2.04 seconds                    │
│ Max Response Time          │ 2.05 seconds                    │
│ Average Response Time      │ 2.04 seconds                    │
│ Median Response Time       │ 2.04 seconds                    │
│ P90 Response Time          │ 2.05 seconds                    │
│ P95 Response Time          │ 2.05 seconds                    │
│ P99 Response Time          │ 2.05 seconds                    │
│ Std Dev Response Time      │ 0.00 seconds                    │
│ Theoretical Max Throughput │ 146.38 requests/second          │
│ Actual Throughput          │ 14.67 requests/second           │
│ Total Generated Tokens     │ 31276                           │
│ Tokens Per Second          │ 1529.23                         │
│ Avg Tokens Per Request     │ 104.25                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘


Test completed in 32.07 seconds
        SGLang Stress Test Results - 2025-04-27 13:42:50        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 32.07 seconds                   │
│ Min Response Time          │ 1.77 seconds                    │
│ Max Response Time          │ 7.87 seconds                    │
│ Average Response Time      │ 2.96 seconds                    │
│ Median Response Time       │ 2.73 seconds                    │
│ P90 Response Time          │ 5.97 seconds                    │
│ P95 Response Time          │ 7.09 seconds                    │
│ P99 Response Time          │ 7.83 seconds                    │
│ Std Dev Response Time      │ 1.48 seconds                    │
│ Theoretical Max Throughput │ 38.12 requests/second           │
│ Actual Throughput          │ 9.35 requests/second            │
│ Total Generated Tokens     │ 31203                           │
│ Tokens Per Second          │ 972.87                          │
│ Avg Tokens Per Request     │ 104.01                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 29.16 seconds
        SGLang Stress Test Results - 2025-04-27 13:43:47        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 29.16 seconds                   │
│ Min Response Time          │ 1.59 seconds                    │
│ Max Response Time          │ 4.04 seconds                    │
│ Average Response Time      │ 2.67 seconds                    │
│ Median Response Time       │ 2.42 seconds                    │
│ P90 Response Time          │ 3.71 seconds                    │
│ P95 Response Time          │ 3.73 seconds                    │
│ P99 Response Time          │ 4.04 seconds                    │
│ Std Dev Response Time      │ 0.69 seconds                    │
│ Theoretical Max Throughput │ 74.18 requests/second           │
│ Actual Throughput          │ 10.29 requests/second           │
│ Total Generated Tokens     │ 31072                           │
│ Tokens Per Second          │ 1065.63                         │
│ Avg Tokens Per Request     │ 103.57                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 39.04 seconds
        SGLang Stress Test Results - 2025-04-27 13:44:49        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 39.04 seconds                   │
│ Min Response Time          │ 1.83 seconds                    │
│ Max Response Time          │ 5.16 seconds                    │
│ Average Response Time      │ 3.29 seconds                    │
│ Median Response Time       │ 3.11 seconds                    │
│ P90 Response Time          │ 4.73 seconds                    │
│ P95 Response Time          │ 5.09 seconds                    │
│ P99 Response Time          │ 5.13 seconds                    │
│ Std Dev Response Time      │ 1.00 seconds                    │
│ Theoretical Max Throughput │ 58.10 requests/second           │
│ Actual Throughput          │ 7.68 requests/second            │
│ Total Generated Tokens     │ 31185                           │
│ Tokens Per Second          │ 798.84                          │
│ Avg Tokens Per Request     │ 103.95                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 32.17 seconds
        SGLang Stress Test Results - 2025-04-27 14:45:36        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 32.16 seconds                   │
│ Min Response Time          │ 2.02 seconds                    │
│ Max Response Time          │ 5.58 seconds                    │
│ Average Response Time      │ 3.01 seconds                    │
│ Median Response Time       │ 2.81 seconds                    │
│ P90 Response Time          │ 4.51 seconds                    │
│ P95 Response Time          │ 4.59 seconds                    │
│ P99 Response Time          │ 5.58 seconds                    │
│ Std Dev Response Time      │ 0.75 seconds                    │
│ Theoretical Max Throughput │ 53.80 requests/second           │
│ Actual Throughput          │ 9.33 requests/second            │
│ Total Generated Tokens     │ 31300                           │
│ Tokens Per Second          │ 973.11                          │
│ Avg Tokens Per Request     │ 104.33                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Prompt: 'Explain what makes a good API in one paragraph....' (47 chars)
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 60.19 seconds
        SGLang Stress Test Results - 2025-04-27 14:47:25        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 60.19 seconds                   │
│ Min Response Time          │ 1.90 seconds                    │
│ Max Response Time          │ 12.31 seconds                   │
│ Average Response Time      │ 4.70 seconds                    │
│ Median Response Time       │ 3.76 seconds                    │
│ P90 Response Time          │ 7.87 seconds                    │
│ P95 Response Time          │ 8.43 seconds                    │
│ P99 Response Time          │ 12.31 seconds                   │
│ Std Dev Response Time      │ 2.57 seconds                    │
│ Theoretical Max Throughput │ 24.37 requests/second           │
│ Actual Throughput          │ 4.98 requests/second            │
│ Total Generated Tokens     │ 31191                           │
│ Tokens Per Second          │ 518.18                          │
│ Avg Tokens Per Request     │ 103.97                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 7.80 seconds
        SGLang Stress Test Results - 2025-04-27 13:45:33        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 5                               │
│ Total Requests             │ 20                              │
│ Successful Requests        │ 20 (100.0%)                     │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 7.80 seconds                    │
│ Min Response Time          │ 1.57 seconds                    │
│ Max Response Time          │ 2.38 seconds                    │
│ Average Response Time      │ 1.92 seconds                    │
│ Median Response Time       │ 1.80 seconds                    │
│ P90 Response Time          │ 2.38 seconds                    │
│ P95 Response Time          │ 2.38 seconds                    │
│ P99 Response Time          │ 2.38 seconds                    │
│ Std Dev Response Time      │ 0.27 seconds                    │
│ Theoretical Max Throughput │ 8.40 requests/second            │
│ Actual Throughput          │ 2.56 requests/second            │
│ Total Generated Tokens     │ 2131                            │
│ Tokens Per Second          │ 273.17                          │
│ Avg Tokens Per Request     │ 106.55                          │
│ Peak Requests In Flight    │ 5                               │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 12.11 seconds
        SGLang Stress Test Results - 2025-04-27 13:45:54        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 5                               │
│ Total Requests             │ 20                              │
│ Successful Requests        │ 20 (100.0%)                     │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 12.11 seconds                   │
│ Min Response Time          │ 1.49 seconds                    │
│ Max Response Time          │ 4.60 seconds                    │
│ Average Response Time      │ 2.95 seconds                    │
│ Median Response Time       │ 2.38 seconds                    │
│ P90 Response Time          │ 4.60 seconds                    │
│ P95 Response Time          │ 4.60 seconds                    │
│ P99 Response Time          │ 4.60 seconds                    │
│ Std Dev Response Time      │ 1.49 seconds                    │
│ Theoretical Max Throughput │ 4.35 requests/second            │
│ Actual Throughput          │ 1.65 requests/second            │
│ Total Generated Tokens     │ 1975                            │
│ Tokens Per Second          │ 163.10                          │
│ Avg Tokens Per Request     │ 98.75                           │
│ Peak Requests In Flight    │ 5                               │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 11.04 seconds
        SGLang Stress Test Results - 2025-04-27 13:50:56        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 5                               │
│ Total Requests             │ 20                              │
│ Successful Requests        │ 20 (100.0%)                     │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 11.04 seconds                   │
│ Min Response Time          │ 1.48 seconds                    │
│ Max Response Time          │ 4.52 seconds                    │
│ Average Response Time      │ 2.52 seconds                    │
│ Median Response Time       │ 1.89 seconds                    │
│ P90 Response Time          │ 4.51 seconds                    │
│ P95 Response Time          │ 4.52 seconds                    │
│ P99 Response Time          │ 4.52 seconds                    │
│ Std Dev Response Time      │ 1.13 seconds                    │
│ Theoretical Max Throughput │ 4.42 requests/second            │
│ Actual Throughput          │ 1.81 requests/second            │
│ Total Generated Tokens     │ 2083                            │
│ Tokens Per Second          │ 188.67                          │
│ Avg Tokens Per Request     │ 104.15                          │
│ Peak Requests In Flight    │ 5                               │
└────────────────────────────┴─────────────────────────────────┘


//再来

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

Test completed in 76.97 seconds
        SGLang Stress Test Results - 2025-04-27 14:02:13        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 76.97 seconds                   │
│ Min Response Time          │ 1.59 seconds                    │
│ Max Response Time          │ 42.59 seconds                   │
│ Average Response Time      │ 5.11 seconds                    │
│ Median Response Time       │ 2.74 seconds                    │
│ P90 Response Time          │ 7.21 seconds                    │
│ P95 Response Time          │ 21.17 seconds                   │
│ P99 Response Time          │ 37.93 seconds                   │
│ Std Dev Response Time      │ 7.00 seconds                    │
│ Theoretical Max Throughput │ 7.04 requests/second            │
│ Actual Throughput          │ 3.90 requests/second            │
│ Total Generated Tokens     │ 31213                           │
│ Tokens Per Second          │ 405.53                          │
│ Avg Tokens Per Request     │ 104.04                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘

Test completed in 42.73 seconds
        SGLang Stress Test Results - 2025-04-27 14:03:19        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 42.73 seconds                   │
│ Min Response Time          │ 1.68 seconds                    │
│ Max Response Time          │ 11.69 seconds                   │
│ Average Response Time      │ 3.51 seconds                    │
│ Median Response Time       │ 3.20 seconds                    │
│ P90 Response Time          │ 4.36 seconds                    │
│ P95 Response Time          │ 5.21 seconds                    │
│ P99 Response Time          │ 11.69 seconds                   │
│ Std Dev Response Time      │ 1.70 seconds                    │
│ Theoretical Max Throughput │ 25.66 requests/second           │
│ Actual Throughput          │ 7.02 requests/second            │
│ Total Generated Tokens     │ 31132                           │
│ Tokens Per Second          │ 728.62                          │
│ Avg Tokens Per Request     │ 103.77                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘


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

Test completed in 49.14 seconds
        SGLang Stress Test Results - 2025-04-27 14:12:23        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                           ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:30000/generate │
│ Max Tokens                 │ 256                             │
│ Concurrent Requests        │ 30                              │
│ Total Requests             │ 300                             │
│ Successful Requests        │ 300 (100.0%)                    │
│ Failed Requests            │ 0 (0.0%)                        │
│ Total Test Duration        │ 49.14 seconds                   │
│ Min Response Time          │ 1.61 seconds                    │
│ Max Response Time          │ 7.47 seconds                    │
│ Average Response Time      │ 3.60 seconds                    │
│ Median Response Time       │ 3.24 seconds                    │
│ P90 Response Time          │ 5.27 seconds                    │
│ P95 Response Time          │ 6.03 seconds                    │
│ P99 Response Time          │ 7.46 seconds                    │
│ Std Dev Response Time      │ 1.36 seconds                    │
│ Theoretical Max Throughput │ 40.14 requests/second           │
│ Actual Throughput          │ 6.11 requests/second            │
│ Total Generated Tokens     │ 31079                           │
│ Tokens Per Second          │ 632.51                          │
│ Avg Tokens Per Request     │ 103.60                          │
│ Peak Requests In Flight    │ 30                              │
└────────────────────────────┴─────────────────────────────────┘
```



### vLLM

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

Test completed in 27.73 seconds
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

Test completed in 28.41 seconds
           vLLM Stress Test Results - 2025-04-27 14:29:22            
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
│ Total Test Duration        │ 28.41 seconds                        │
│ Min Response Time          │ 1.36 seconds                         │
│ Max Response Time          │ 3.53 seconds                         │
│ Average Response Time      │ 2.28 seconds                         │
│ Median Response Time       │ 2.28 seconds                         │
│ P90 Response Time          │ 2.57 seconds                         │
│ P95 Response Time          │ 2.67 seconds                         │
│ P99 Response Time          │ 2.96 seconds                         │
│ Std Dev Response Time      │ 0.26 seconds                         │
│ Theoretical Max Throughput │ 85.09 requests/second                │
│ Actual Throughput          │ 10.56 requests/second                │
│ Total Generated Tokens     │ 29861                                │
│ Tokens Per Second          │ 1051.13                              │
│ Avg Tokens Per Request     │ 99.54                                │
│ Peak Requests In Flight    │ 30                                   │
└────────────────────────────┴──────────────────────────────────────┘

root@iZ2zed7pdsnsrie8263p0kZ:/home# ./vllm-stress-test.py --concurrent 5 --total 20
Starting vLLM Stress Test
URL: http://localhost:8000/v1/completions
Model: /home/vllm/llm/Qwen7B-awq
Max Tokens: 256
Temperature: 0.7
Concurrent requests: 5
Total requests: 20
Prompt: 'Explain what makes a good API in one paragraph....' (47 chars)
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 5.52 seconds
           vLLM Stress Test Results - 2025-04-27 14:27:41            
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
│ Total Test Duration        │ 5.52 seconds                         │
│ Min Response Time          │ 0.96 seconds                         │
│ Max Response Time          │ 1.44 seconds                         │
│ Average Response Time      │ 1.23 seconds                         │
│ Median Response Time       │ 1.22 seconds                         │
│ P90 Response Time          │ 1.39 seconds                         │
│ P95 Response Time          │ 1.44 seconds                         │
│ P99 Response Time          │ 1.44 seconds                         │
│ Std Dev Response Time      │ 0.14 seconds                         │
│ Theoretical Max Throughput │ 13.89 requests/second                │
│ Actual Throughput          │ 3.62 requests/second                 │
│ Total Generated Tokens     │ 1981                                 │
│ Tokens Per Second          │ 358.69                               │
│ Avg Tokens Per Request     │ 99.05                                │
│ Peak Requests In Flight    │ 5                                    │
└────────────────────────────┴──────────────────────────────────────┘
root@iZ2zed7pdsnsrie8263p0kZ:/home# ./vllm-stress-test.py --concurrent 5 --total 20
Starting vLLM Stress Test
URL: http://localhost:8000/v1/completions
Model: /home/vllm/llm/Qwen7B-awq
Max Tokens: 256
Temperature: 0.7
Concurrent requests: 5
Total requests: 20
Prompt: 'Explain what makes a good API in one paragraph....' (47 chars)
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 5.53 seconds
           vLLM Stress Test Results - 2025-04-27 14:28:04            
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
│ Total Test Duration        │ 5.53 seconds                         │
│ Min Response Time          │ 0.78 seconds                         │
│ Max Response Time          │ 1.50 seconds                         │
│ Average Response Time      │ 1.18 seconds                         │
│ Median Response Time       │ 1.15 seconds                         │
│ P90 Response Time          │ 1.40 seconds                         │
│ P95 Response Time          │ 1.50 seconds                         │
│ P99 Response Time          │ 1.50 seconds                         │
│ Std Dev Response Time      │ 0.16 seconds                         │
│ Theoretical Max Throughput │ 13.33 requests/second                │
│ Actual Throughput          │ 3.62 requests/second                 │
│ Total Generated Tokens     │ 1908                                 │
│ Tokens Per Second          │ 345.18                               │
│ Avg Tokens Per Request     │ 95.40                                │
│ Peak Requests In Flight    │ 5                                    │
└────────────────────────────┴──────────────────────────────────────┘
```

