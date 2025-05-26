## openai api

### vLLM

```
----------- think ---------------

Test completed in 259.13 seconds
        LLM Stress Test Results - 2025-05-26 15:25:44        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 3096                         │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 259.13 seconds               │
│ Min Response Time          │ 4.05 seconds                 │
│ Max Response Time          │ 30.49 seconds                │
│ Average Response Time      │ 16.64 seconds                │
│ Median Response Time       │ 17.01 seconds                │
│ P90 Response Time          │ 25.15 seconds                │
│ P95 Response Time          │ 27.17 seconds                │
│ P99 Response Time          │ 30.49 seconds                │
│ Std Dev Response Time      │ 6.91 seconds                 │
│ Theoretical Max Throughput │ 3.28 requests/second         │
│ Actual Throughput          │ 0.39 requests/second         │
│ Total Generated Tokens     │ 97944                        │
│ Tokens Per Second          │ 377.98                       │
│ Avg Tokens Per Request     │ 979.44                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘

Test completed in 259.25 seconds
        LLM Stress Test Results - 2025-05-26 15:31:35        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 3096                         │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 259.24 seconds               │
│ Min Response Time          │ 4.91 seconds                 │
│ Max Response Time          │ 29.94 seconds                │
│ Average Response Time      │ 17.54 seconds                │
│ Median Response Time       │ 18.00 seconds                │
│ P90 Response Time          │ 25.53 seconds                │
│ P95 Response Time          │ 26.62 seconds                │
│ P99 Response Time          │ 29.94 seconds                │
│ Std Dev Response Time      │ 6.53 seconds                 │
│ Theoretical Max Throughput │ 3.34 requests/second         │
│ Actual Throughput          │ 0.39 requests/second         │
│ Total Generated Tokens     │ 102432                       │
│ Tokens Per Second          │ 395.12                       │
│ Avg Tokens Per Request     │ 1024.32                      │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘


--------------- no think  ---------------------

Test completed in 150.45 seconds
        LLM Stress Test Results - 2025-05-26 15:36:29        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 3096                         │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 150.45 seconds               │
│ Min Response Time          │ 0.95 seconds                 │
│ Max Response Time          │ 18.19 seconds                │
│ Average Response Time      │ 7.01 seconds                 │
│ Median Response Time       │ 5.94 seconds                 │
│ P90 Response Time          │ 13.08 seconds                │
│ P95 Response Time          │ 16.43 seconds                │
│ P99 Response Time          │ 18.19 seconds                │
│ Std Dev Response Time      │ 4.40 seconds                 │
│ Theoretical Max Throughput │ 5.50 requests/second         │
│ Actual Throughput          │ 0.66 requests/second         │
│ Total Generated Tokens     │ 41934                        │
│ Tokens Per Second          │ 278.73                       │
│ Avg Tokens Per Request     │ 419.34                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘

Test completed in 142.93 seconds
        LLM Stress Test Results - 2025-05-26 15:39:27        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 3096                         │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 142.93 seconds               │
│ Min Response Time          │ 0.99 seconds                 │
│ Max Response Time          │ 17.49 seconds                │
│ Average Response Time      │ 5.98 seconds                 │
│ Median Response Time       │ 4.26 seconds                 │
│ P90 Response Time          │ 13.71 seconds                │
│ P95 Response Time          │ 16.09 seconds                │
│ P99 Response Time          │ 17.49 seconds                │
│ Std Dev Response Time      │ 4.71 seconds                 │
│ Theoretical Max Throughput │ 5.72 requests/second         │
│ Actual Throughput          │ 0.70 requests/second         │
│ Total Generated Tokens     │ 35731                        │
│ Tokens Per Second          │ 249.99                       │
│ Avg Tokens Per Request     │ 357.31                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘
```

### SGLang

```
--------------- no think  ---------------------

Test completed in 168.77 seconds
        LLM Stress Test Results - 2025-05-26 15:48:58        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 3096                         │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 168.77 seconds               │
│ Min Response Time          │ 1.69 seconds                 │
│ Max Response Time          │ 28.53 seconds                │
│ Average Response Time      │ 8.94 seconds                 │
│ Median Response Time       │ 6.77 seconds                 │
│ P90 Response Time          │ 19.67 seconds                │
│ P95 Response Time          │ 20.74 seconds                │
│ P99 Response Time          │ 28.53 seconds                │
│ Std Dev Response Time      │ 6.18 seconds                 │
│ Theoretical Max Throughput │ 3.50 requests/second         │
│ Actual Throughput          │ 0.59 requests/second         │
│ Total Generated Tokens     │ 40203                        │
│ Tokens Per Second          │ 238.21                       │
│ Avg Tokens Per Request     │ 402.03                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘

Test completed in 175.35 seconds
        LLM Stress Test Results - 2025-05-26 15:52:09        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 3096                         │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 175.35 seconds               │
│ Min Response Time          │ 1.69 seconds                 │
│ Max Response Time          │ 29.54 seconds                │
│ Average Response Time      │ 7.82 seconds                 │
│ Median Response Time       │ 5.90 seconds                 │
│ P90 Response Time          │ 16.51 seconds                │
│ P95 Response Time          │ 17.72 seconds                │
│ P99 Response Time          │ 29.54 seconds                │
│ Std Dev Response Time      │ 5.57 seconds                 │
│ Theoretical Max Throughput │ 3.39 requests/second         │
│ Actual Throughput          │ 0.57 requests/second         │
│ Total Generated Tokens     │ 42052                        │
│ Tokens Per Second          │ 239.82                       │
│ Avg Tokens Per Request     │ 420.52                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘


----------- think ---------------
Test completed in 276.74 seconds
        LLM Stress Test Results - 2025-05-26 15:58:40        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 3096                         │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 276.74 seconds               │
│ Min Response Time          │ 6.18 seconds                 │
│ Max Response Time          │ 33.10 seconds                │
│ Average Response Time      │ 18.59 seconds                │
│ Median Response Time       │ 19.22 seconds                │
│ P90 Response Time          │ 29.12 seconds                │
│ P95 Response Time          │ 30.29 seconds                │
│ P99 Response Time          │ 33.10 seconds                │
│ Std Dev Response Time      │ 7.64 seconds                 │
│ Theoretical Max Throughput │ 3.02 requests/second         │
│ Actual Throughput          │ 0.36 requests/second         │
│ Total Generated Tokens     │ 93307                        │
│ Tokens Per Second          │ 337.17                       │
│ Avg Tokens Per Request     │ 933.07                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘

Test completed in 265.98 seconds
        LLM Stress Test Results - 2025-05-26 16:04:23        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 3096                         │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 265.98 seconds               │
│ Min Response Time          │ 6.46 seconds                 │
│ Max Response Time          │ 33.59 seconds                │
│ Average Response Time      │ 19.10 seconds                │
│ Median Response Time       │ 19.42 seconds                │
│ P90 Response Time          │ 27.99 seconds                │
│ P95 Response Time          │ 29.30 seconds                │
│ P99 Response Time          │ 33.59 seconds                │
│ Std Dev Response Time      │ 6.84 seconds                 │
│ Theoretical Max Throughput │ 2.98 requests/second         │
│ Actual Throughput          │ 0.38 requests/second         │
│ Total Generated Tokens     │ 98199                        │
│ Tokens Per Second          │ 369.19                       │
│ Avg Tokens Per Request     │ 981.99                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘
```



### max_token 512 with no think mode



```
---- sglang ----
Test completed in 60.86 seconds
        LLM Stress Test Results - 2025-05-26 17:15:58        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 512                          │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 60.86 seconds                │
│ Min Response Time          │ 1.54 seconds                 │
│ Max Response Time          │ 7.18 seconds                 │
│ Average Response Time      │ 4.59 seconds                 │
│ Median Response Time       │ 5.23 seconds                 │
│ P90 Response Time          │ 6.75 seconds                 │
│ P95 Response Time          │ 7.17 seconds                 │
│ P99 Response Time          │ 7.18 seconds                 │
│ Std Dev Response Time      │ 1.74 seconds                 │
│ Theoretical Max Throughput │ 13.93 requests/second        │
│ Actual Throughput          │ 1.64 requests/second         │
│ Total Generated Tokens     │ 24421                        │
│ Tokens Per Second          │ 401.26                       │
│ Avg Tokens Per Request     │ 244.21                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘

Test completed in 64.16 seconds
        LLM Stress Test Results - 2025-05-26 17:17:46        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 512                          │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 64.16 seconds                │
│ Min Response Time          │ 1.79 seconds                 │
│ Max Response Time          │ 7.30 seconds                 │
│ Average Response Time      │ 5.24 seconds                 │
│ Median Response Time       │ 5.88 seconds                 │
│ P90 Response Time          │ 7.16 seconds                 │
│ P95 Response Time          │ 7.29 seconds                 │
│ P99 Response Time          │ 7.30 seconds                 │
│ Std Dev Response Time      │ 1.70 seconds                 │
│ Theoretical Max Throughput │ 13.69 requests/second        │
│ Actual Throughput          │ 1.56 requests/second         │
│ Total Generated Tokens     │ 26533                        │
│ Tokens Per Second          │ 413.54                       │
│ Avg Tokens Per Request     │ 265.33                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘


---- vllm ----

Test completed in 58.45 seconds
        LLM Stress Test Results - 2025-05-26 17:20:49        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 512                          │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 58.45 seconds                │
│ Min Response Time          │ 1.26 seconds                 │
│ Max Response Time          │ 6.26 seconds                 │
│ Average Response Time      │ 4.67 seconds                 │
│ Median Response Time       │ 5.67 seconds                 │
│ P90 Response Time          │ 5.87 seconds                 │
│ P95 Response Time          │ 6.15 seconds                 │
│ P99 Response Time          │ 6.26 seconds                 │
│ Std Dev Response Time      │ 1.57 seconds                 │
│ Theoretical Max Throughput │ 15.98 requests/second        │
│ Actual Throughput          │ 1.71 requests/second         │
│ Total Generated Tokens     │ 27450                        │
│ Tokens Per Second          │ 469.62                       │
│ Avg Tokens Per Request     │ 274.50                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘

Test completed in 57.02 seconds
        LLM Stress Test Results - 2025-05-26 17:22:12        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B │
│ Max Tokens                 │ 512                          │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 57.02 seconds                │
│ Min Response Time          │ 0.99 seconds                 │
│ Max Response Time          │ 5.85 seconds                 │
│ Average Response Time      │ 4.10 seconds                 │
│ Median Response Time       │ 5.36 seconds                 │
│ P90 Response Time          │ 5.78 seconds                 │
│ P95 Response Time          │ 5.84 seconds                 │
│ P99 Response Time          │ 5.85 seconds                 │
│ Std Dev Response Time      │ 1.82 seconds                 │
│ Theoretical Max Throughput │ 17.10 requests/second        │
│ Actual Throughput          │ 1.75 requests/second         │
│ Total Generated Tokens     │ 24735                        │
│ Tokens Per Second          │ 433.77                       │
│ Avg Tokens Per Request     │ 247.35                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘
```





## native api

### vLLM

```
Test completed in 59.82 seconds
           vLLM Stress Test Results - 2025-05-26 16:58:12            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:8000/v1/completions │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B         │
│ Max Tokens                 │ 512                                  │
│ Temperature                │ 0.7                                  │
│ Concurrent Requests        │ 10                                   │
│ Total Requests             │ 100                                  │
│ Successful Requests        │ 100 (100.0%)                         │
│ Failed Requests            │ 0 (0.0%)                             │
│ Total Test Duration        │ 59.82 seconds                        │
│ Min Response Time          │ 4.90 seconds                         │
│ Max Response Time          │ 6.03 seconds                         │
│ Average Response Time      │ 5.96 seconds                         │
│ Median Response Time       │ 5.98 seconds                         │
│ P90 Response Time          │ 6.00 seconds                         │
│ P95 Response Time          │ 6.02 seconds                         │
│ P99 Response Time          │ 6.03 seconds                         │
│ Std Dev Response Time      │ 0.11 seconds                         │
│ Theoretical Max Throughput │ 16.60 requests/second                │
│ Actual Throughput          │ 1.67 requests/second                 │
│ Total Generated Tokens     │ 39279                                │
│ Tokens Per Second          │ 656.60                               │
│ Avg Tokens Per Request     │ 392.79                               │
│ Peak Requests In Flight    │ 10                                   │
└────────────────────────────┴──────────────────────────────────────┘

Test completed in 128.75 seconds
           vLLM Stress Test Results - 2025-05-26 17:06:11            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                                ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:8000/v1/completions │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-4B         │
│ Max Tokens                 │ 1024                                 │
│ Temperature                │ 0.7                                  │
│ Concurrent Requests        │ 10                                   │
│ Total Requests             │ 100                                  │
│ Successful Requests        │ 100 (100.0%)                         │
│ Failed Requests            │ 0 (0.0%)                             │
│ Total Test Duration        │ 128.75 seconds                       │
│ Min Response Time          │ 11.59 seconds                        │
│ Max Response Time          │ 12.94 seconds                        │
│ Average Response Time      │ 12.85 seconds                        │
│ Median Response Time       │ 12.87 seconds                        │
│ P90 Response Time          │ 12.92 seconds                        │
│ P95 Response Time          │ 12.93 seconds                        │
│ P99 Response Time          │ 12.94 seconds                        │
│ Std Dev Response Time      │ 0.14 seconds                         │
│ Theoretical Max Throughput │ 7.73 requests/second                 │
│ Actual Throughput          │ 0.78 requests/second                 │
│ Total Generated Tokens     │ 78276                                │
│ Tokens Per Second          │ 607.98                               │
│ Avg Tokens Per Request     │ 782.76                               │
│ Peak Requests In Flight    │ 10                                   │
└────────────────────────────┴──────────────────────────────────────┘
```



### SGLang

completion_tokens is always 128

```
{'text': ' Also, explain the difference between "technical debt" and "equity debt". I understand the ROI, but I don\'t get the ROI in the 
code. What\'s the ROI in code? I have a concern that my code is in a "technical debt" situation, but I can\'t see it. How to check if I\'m 
in a "technical debt" situation? How do I spot "technical debt" in code?\n\nLet me also explain how I have fallen into the quagmire and how 
I have been managing what I have. I was managing a project where a lot of science research is done in code, but', 'meta_info': {'id': 
'1ce23143fe0748b8a1d01c9a21279a55', 'finish_reason': {'type': 'length', 'length': 128}, 'prompt_tokens': 13, 'completion_tokens': 128, 
'cached_tokens': 12, 'e2e_latency': 2.365816116333008}}
{'text': " The CAP theorem says that in a distributed system, it's impossible to have all three of consistency, availability, and partition 
tolerance at the same time. So, you have to make trade-offs between them. For example, if you have a system that's not partitioned (no 
network issues), then you can have both consistency and availability. But if there are partitions (network issues), then you have to choose 
between consistency and availability. For example, if you choose consistency, then you have to sacrifice availability (so you can't read or 
write data until the partition is resolved). If you choose availability, then you have to sacrifice consistency (", 'meta_info': {'id': 
'd9dfe0305e534ca7bf2a5307aa5a5f0f', 'finish_reason': {'type': 'length', 'length': 128}, 'prompt_tokens': 9, 'completion_tokens': 128, 
'cached_tokens': 8, 'e2e_latency': 2.365438461303711}}


Test completed in 23.94 seconds
       SGLang Stress Test Results - 2025-05-26 17:10:35        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:8000/generate │
│ Max Tokens                 │ 512                            │
│ Concurrent Requests        │ 10                             │
│ Total Requests             │ 100                            │
│ Successful Requests        │ 100 (100.0%)                   │
│ Failed Requests            │ 0 (0.0%)                       │
│ Total Test Duration        │ 23.94 seconds                  │
│ Min Response Time          │ 2.35 seconds                   │
│ Max Response Time          │ 2.43 seconds                   │
│ Average Response Time      │ 2.39 seconds                   │
│ Median Response Time       │ 2.39 seconds                   │
│ P90 Response Time          │ 2.42 seconds                   │
│ P95 Response Time          │ 2.43 seconds                   │
│ P99 Response Time          │ 2.43 seconds                   │
│ Std Dev Response Time      │ 0.02 seconds                   │
│ Theoretical Max Throughput │ 41.18 requests/second          │
│ Actual Throughput          │ 4.18 requests/second           │
│ Total Generated Tokens     │ 10165                          │
│ Tokens Per Second          │ 424.58                         │
│ Avg Tokens Per Request     │ 101.65                         │
│ Peak Requests In Flight    │ 10                             │
└────────────────────────────┴────────────────────────────────┘

Test completed in 23.97 seconds
       SGLang Stress Test Results - 2025-05-26 17:11:28        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                          ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ URL                        │ http://localhost:8000/generate │
│ Max Tokens                 │ 1024                           │
│ Concurrent Requests        │ 10                             │
│ Total Requests             │ 100                            │
│ Successful Requests        │ 100 (100.0%)                   │
│ Failed Requests            │ 0 (0.0%)                       │
│ Total Test Duration        │ 23.97 seconds                  │
│ Min Response Time          │ 2.38 seconds                   │
│ Max Response Time          │ 2.41 seconds                   │
│ Average Response Time      │ 2.39 seconds                   │
│ Median Response Time       │ 2.39 seconds                   │
│ P90 Response Time          │ 2.40 seconds                   │
│ P95 Response Time          │ 2.40 seconds                   │
│ P99 Response Time          │ 2.41 seconds                   │
│ Std Dev Response Time      │ 0.01 seconds                   │
│ Theoretical Max Throughput │ 41.57 requests/second          │
│ Actual Throughput          │ 4.17 requests/second           │
│ Total Generated Tokens     │ 10144                          │
│ Tokens Per Second          │ 423.26                         │
│ Avg Tokens Per Request     │ 101.44                         │
│ Peak Requests In Flight    │ 10                             │
└────────────────────────────┴────────────────────────────────┘

```

