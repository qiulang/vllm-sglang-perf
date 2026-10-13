```
# vllm
(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$ python qwen3_openai_stress_test.py
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: qwen3-14b
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 10
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 34.58 seconds
         LLM Stress Test Results - 2026-10-13 10:44:01
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
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 34.58 seconds            │
│ Min Response Time                 │ 1.18 seconds             │
│ Max Response Time                 │ 3.53 seconds             │
│ Average Response Time             │ 3.24 seconds             │
│ Median Response Time              │ 3.51 seconds             │
│ P90 Response Time                 │ 3.52 seconds             │
│ P95 Response Time                 │ 3.52 seconds             │
│ P99 Response Time                 │ 3.53 seconds             │
│ Std Dev Response Time             │ 0.64 seconds             │
│ Theoretical Max Throughput        │ 28.31 requests/second    │
│ Actual Throughput                 │ 2.89 requests/second     │
│ Total Completion Tokens           │ 23675                    │
│ Total Prompt Tokens               │ 2236                     │
│ Total Tokens                      │ 25911                    │
│ Completion Tokens Per Second      │ 684.64                   │
│ Avg Completion Tokens Per Request │ 236.75                   │
│ Peak Requests In Flight           │ 10                       │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
Containers and virtual machines (VMs) are both used for running applications in isolated environments, but they differ significantly in terms of
architecture, resource usage, performance, and use case...
(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$

(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$ python qwen3_openai_stress_test.py --concurrent 20 --total 200
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: qwen3-14b
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 20
Total requests: 200
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 38.09 seconds
         LLM Stress Test Results - 2026-10-13 10:47:54
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ qwen3-14b                │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 20                       │
│ Total Requests                    │ 200                      │
│ Successful Requests               │ 200 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 38.09 seconds            │
│ Min Response Time                 │ 1.21 seconds             │
│ Max Response Time                 │ 3.87 seconds             │
│ Average Response Time             │ 3.63 seconds             │
│ Median Response Time              │ 3.85 seconds             │
│ P90 Response Time                 │ 3.86 seconds             │
│ P95 Response Time                 │ 3.87 seconds             │
│ P99 Response Time                 │ 3.87 seconds             │
│ Std Dev Response Time             │ 0.61 seconds             │
│ Theoretical Max Throughput        │ 51.67 requests/second    │
│ Actual Throughput                 │ 5.25 requests/second     │
│ Total Completion Tokens           │ 48355                    │
│ Total Prompt Tokens               │ 4441                     │
│ Total Tokens                      │ 52796                    │
│ Completion Tokens Per Second      │ 1269.45                  │
│ Avg Completion Tokens Per Request │ 241.78                   │
│ Peak Requests In Flight           │ 20                       │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
Microservices architecture is a design approach that structures an application as a collection of loosely coupled, independently deployable services. It
has become increasingly popular for building sc...
(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$

(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$ python qwen3_openai_stress_test.py --enable-thinking false --concurrent 30 --total 300
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: qwen3-14b
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: False
Concurrent requests: 30
Total requests: 300
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 40.47 seconds
         LLM Stress Test Results - 2026-10-13 11:52:49
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ qwen3-14b                │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ False                    │
│ Concurrent Requests               │ 30                       │
│ Total Requests                    │ 300                      │
│ Successful Requests               │ 300 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 40.47 seconds            │
│ Min Response Time                 │ 1.42 seconds             │
│ Max Response Time                 │ 4.10 seconds             │
│ Average Response Time             │ 3.89 seconds             │
│ Median Response Time              │ 4.07 seconds             │
│ P90 Response Time                 │ 4.09 seconds             │
│ P95 Response Time                 │ 4.09 seconds             │
│ P99 Response Time                 │ 4.10 seconds             │
│ Std Dev Response Time             │ 0.54 seconds             │
│ Theoretical Max Throughput        │ 73.09 requests/second    │
│ Actual Throughput                 │ 7.41 requests/second     │
│ Total Completion Tokens           │ 73562                    │
│ Total Prompt Tokens               │ 6676                     │
│ Total Tokens                      │ 80238                    │
│ Completion Tokens Per Second      │ 1817.81                  │
│ Avg Completion Tokens Per Request │ 245.21                   │
│ Peak Requests In Flight           │ 30                       │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
Sure! Here's a simple way to explain technical debt to a non-technical person:

Imagine you're building a house. You're in a hurry to get it done, so instead of taking the time to lay a strong, proper...
(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$

# sgang

(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$ python qwen3_openai_stress_test.py --enable-thinking false --total 1
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: qwen3-14b
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: False
Concurrent requests: 10
Total requests: 1
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
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

Sample Responses:
Sample without Thinking:
DNS resolution is the process by which a domain name (e.g., `example.com`) is translated into an IP address (e.g., `93.184.216.34`) so that a computer
can locate and connect to the appropriate server ...
(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$ python qwen3_openai_stress_test.py --enable-thinking false
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: qwen3-14b
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: False
Concurrent requests: 10
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 36.14 seconds
         LLM Stress Test Results - 2026-10-13 11:21:00
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
│ Total Test Duration               │ 36.14 seconds            │
│ Min Response Time                 │ 1.17 seconds             │
│ Max Response Time                 │ 3.78 seconds             │
│ Average Response Time             │ 3.41 seconds             │
│ Median Response Time              │ 3.62 seconds             │
│ P90 Response Time                 │ 3.66 seconds             │
│ P95 Response Time                 │ 3.78 seconds             │
│ P99 Response Time                 │ 3.78 seconds             │
│ Std Dev Response Time             │ 0.61 seconds             │
│ Theoretical Max Throughput        │ 26.44 requests/second    │
│ Actual Throughput                 │ 2.77 requests/second     │
│ Total Completion Tokens           │ 24060                    │
│ Total Prompt Tokens               │ 2203                     │
│ Total Tokens                      │ 26263                    │
│ Completion Tokens Per Second      │ 665.74                   │
│ Avg Completion Tokens Per Request │ 240.60                   │
│ Peak Requests In Flight           │ 10                       │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
When designing a distributed system, there are several key considerations to ensure reliability, scalability, and performance. Three of the most
important ones are:

1. **Fault Tolerance**
   Distri...
(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$

(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$ python qwen3_openai_stress_test.py --enable-thinking false --concurrent 20 --total 200
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: qwen3-14b
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: False
Concurrent requests: 20
Total requests: 200
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 40.99 seconds
         LLM Stress Test Results - 2026-10-13 11:28:00
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
│ Total Test Duration               │ 40.99 seconds            │
│ Min Response Time                 │ 1.41 seconds             │
│ Max Response Time                 │ 4.24 seconds             │
│ Average Response Time             │ 3.92 seconds             │
│ Median Response Time              │ 4.13 seconds             │
│ P90 Response Time                 │ 4.22 seconds             │
│ P95 Response Time                 │ 4.23 seconds             │
│ P99 Response Time                 │ 4.24 seconds             │
│ Std Dev Response Time             │ 0.62 seconds             │
│ Theoretical Max Throughput        │ 47.12 requests/second    │
│ Actual Throughput                 │ 4.88 requests/second     │
│ Total Completion Tokens           │ 48612                    │
│ Total Prompt Tokens               │ 4477                     │
│ Total Tokens                      │ 53089                    │
│ Completion Tokens Per Second      │ 1185.90                  │
│ Avg Completion Tokens Per Request │ 243.06                   │
│ Peak Requests In Flight           │ 20                       │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
REST (Representational State Transfer) is an architectural style for designing networked applications, particularly web services. It is not a standard or
protocol but a set of constraints and principl...
(vllm_env) vllm@iZbp12jw6pq7qqi0v02jqcZ:~/test$
```

