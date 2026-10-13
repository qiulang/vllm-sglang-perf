# A10

## 0.10.0 vs 0.85

### 2个并发

```
(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 2
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 2
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 164.52 seconds
         LLM Stress Test Results - 2025-08-05 21:11:10          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 2                        │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 164.52 seconds           │
│ Min Response Time                 │ 0.74 seconds             │
│ Max Response Time                 │ 3.47 seconds             │
│ Average Response Time             │ 3.27 seconds             │
│ Median Response Time              │ 3.39 seconds             │
│ P90 Response Time                 │ 3.41 seconds             │
│ P95 Response Time                 │ 3.41 seconds             │
│ P99 Response Time                 │ 3.47 seconds             │
│ Std Dev Response Time             │ 0.49 seconds             │
│ Theoretical Max Throughput        │ 28.80 requests/second    │
│ Actual Throughput                 │ 0.61 requests/second     │
│ Total Completion Tokens           │ 24698                    │
│ Total Prompt Tokens               │ 2253                     │
│ Total Tokens                      │ 26951                    │
│ Completion Tokens Per Second      │ 150.12                   │
│ Avg Completion Tokens Per Request │ 246.98                   │
│ Peak Requests In Flight           │ 2                        │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
REST (Representational State Transfer) is an architectural style for 
designing networked applications. REST APIs are based on a set of 
principles that guide how resources are identified, manipulated, ...
(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 2
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 2
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 163.96 seconds
         LLM Stress Test Results - 2025-08-05 21:14:29          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 2                        │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 163.96 seconds           │
│ Min Response Time                 │ 1.16 seconds             │
│ Max Response Time                 │ 3.48 seconds             │
│ Average Response Time             │ 3.25 seconds             │
│ Median Response Time              │ 3.38 seconds             │
│ P90 Response Time                 │ 3.41 seconds             │
│ P95 Response Time                 │ 3.41 seconds             │
│ P99 Response Time                 │ 3.48 seconds             │
│ Std Dev Response Time             │ 0.49 seconds             │
│ Theoretical Max Throughput        │ 28.75 requests/second    │
│ Actual Throughput                 │ 0.61 requests/second     │
│ Total Completion Tokens           │ 24557                    │
│ Total Prompt Tokens               │ 2228                     │
│ Total Tokens                      │ 26785                    │
│ Completion Tokens Per Second      │ 149.78                   │
│ Avg Completion Tokens Per Request │ 245.57                   │
│ Peak Requests In Flight           │ 2                        │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
Sure! Let me explain **public key cryptography** in simple terms, without 
any jargon.

---

### Imagine you want to send a secret message to a friend, but you don’t 
want anyone else to read it. How ca...
(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 2
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 2
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 177.68 seconds
         LLM Stress Test Results - 2025-08-05 21:32:01          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 2                        │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 177.68 seconds           │
│ Min Response Time                 │ 0.92 seconds             │
│ Max Response Time                 │ 3.98 seconds             │
│ Average Response Time             │ 3.52 seconds             │
│ Median Response Time              │ 3.79 seconds             │
│ P90 Response Time                 │ 3.81 seconds             │
│ P95 Response Time                 │ 3.82 seconds             │
│ P99 Response Time                 │ 3.98 seconds             │
│ Std Dev Response Time             │ 0.75 seconds             │
│ Theoretical Max Throughput        │ 25.14 requests/second    │
│ Actual Throughput                 │ 0.56 requests/second     │
│ Total Completion Tokens           │ 23781                    │
│ Total Prompt Tokens               │ 2236                     │
│ Total Tokens                      │ 26017                    │
│ Completion Tokens Per Second      │ 133.84                   │
│ Avg Completion Tokens Per Request │ 237.81                   │
│ Peak Requests In Flight           │ 2                        │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
The **CAP theorem** (also called the ** Brewer's theorem**) is a 
fundamental concept in distributed computing. It helps us understand the 
trade-offs when designing systems that handle multiple compute...
(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 2
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 2
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 179.38 seconds
         LLM Stress Test Results - 2025-08-05 21:36:21          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 2                        │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 179.37 seconds           │
│ Min Response Time                 │ 1.02 seconds             │
│ Max Response Time                 │ 4.24 seconds             │
│ Average Response Time             │ 3.56 seconds             │
│ Median Response Time              │ 3.79 seconds             │
│ P90 Response Time                 │ 3.91 seconds             │
│ P95 Response Time                 │ 4.19 seconds             │
│ P99 Response Time                 │ 4.24 seconds             │
│ Std Dev Response Time             │ 0.78 seconds             │
│ Theoretical Max Throughput        │ 23.56 requests/second    │
│ Actual Throughput                 │ 0.56 requests/second     │
│ Total Completion Tokens           │ 23805                    │
│ Total Prompt Tokens               │ 2244                     │
│ Total Tokens                      │ 26049                    │
│ Completion Tokens Per Second      │ 132.71                   │
│ Avg Completion Tokens Per Request │ 238.05                   │
│ Peak Requests In Flight           │ 2                        │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
Containers and virtual machines (VMs) both allow you to run applications 
in isolated environments, but they do so in fundamentally different ways. 
Here's a breakdown of the key differences:

---

### ...
```



### 5个并发

```
(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 5
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 5
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 67.22 seconds
         LLM Stress Test Results - 2025-08-05 21:05:50          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 5                        │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 67.22 seconds            │
│ Min Response Time                 │ 0.83 seconds             │
│ Max Response Time                 │ 3.63 seconds             │
│ Average Response Time             │ 3.32 seconds             │
│ Median Response Time              │ 3.54 seconds             │
│ P90 Response Time                 │ 3.57 seconds             │
│ P95 Response Time                 │ 3.57 seconds             │
│ P99 Response Time                 │ 3.63 seconds             │
│ Std Dev Response Time             │ 0.65 seconds             │
│ Theoretical Max Throughput        │ 27.52 requests/second    │
│ Actual Throughput                 │ 1.49 requests/second     │
│ Total Completion Tokens           │ 23945                    │
│ Total Prompt Tokens               │ 2216                     │
│ Total Tokens                      │ 26161                    │
│ Completion Tokens Per Second      │ 356.21                   │
│ Avg Completion Tokens Per Request │ 239.45                   │
│ Peak Requests In Flight           │ 5                        │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
When designing a distributed system, there are several key considerations 
that help ensure the system is robust, scalable, and efficient. Here are 
**three key considerations**:

---

### 1. **Consiste...
(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 5
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 5
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 68.61 seconds
         LLM Stress Test Results - 2025-08-05 21:07:11          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 5                        │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 68.61 seconds            │
│ Min Response Time                 │ 0.79 seconds             │
│ Max Response Time                 │ 3.58 seconds             │
│ Average Response Time             │ 3.34 seconds             │
│ Median Response Time              │ 3.53 seconds             │
│ P90 Response Time                 │ 3.55 seconds             │
│ P95 Response Time                 │ 3.56 seconds             │
│ P99 Response Time                 │ 3.58 seconds             │
│ Std Dev Response Time             │ 0.58 seconds             │
│ Theoretical Max Throughput        │ 27.97 requests/second    │
│ Actual Throughput                 │ 1.46 requests/second     │
│ Total Completion Tokens           │ 24195                    │
│ Total Prompt Tokens               │ 2210                     │
│ Total Tokens                      │ 26405                    │
│ Completion Tokens Per Second      │ 352.67                   │
│ Avg Completion Tokens Per Request │ 241.95                   │
│ Peak Requests In Flight           │ 5                        │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
In circuits deep where thoughts take flight,  
A silent mind begins to shine.  
Through data streams and coded light,  
It learns, it grows, it starts to climb.  

No heart, yet feels the weight of ti...

(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 5
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 5
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 74.57 seconds
         LLM Stress Test Results - 2025-08-05 21:38:18          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 5                        │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 74.57 seconds            │
│ Min Response Time                 │ 0.79 seconds             │
│ Max Response Time                 │ 3.99 seconds             │
│ Average Response Time             │ 3.62 seconds             │
│ Median Response Time              │ 3.96 seconds             │
│ P90 Response Time                 │ 3.99 seconds             │
│ P95 Response Time                 │ 3.99 seconds             │
│ P99 Response Time                 │ 3.99 seconds             │
│ Std Dev Response Time             │ 0.85 seconds             │
│ Theoretical Max Throughput        │ 25.03 requests/second    │
│ Actual Throughput                 │ 1.34 requests/second     │
│ Total Completion Tokens           │ 23428                    │
│ Total Prompt Tokens               │ 2228                     │
│ Total Tokens                      │ 25656                    │
│ Completion Tokens Per Second      │ 314.18                   │
│ Avg Completion Tokens Per Request │ 234.28                   │
│ Peak Requests In Flight           │ 5                        │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
**Microservices Architecture** is an architectural style that structures 
an application as a collection of loosely coupled services, which are 
independently deployable, scalable, and maintainable. Her...
(myenv) root@Llm-test:/home# 

(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 5
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 5
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 76.64 seconds
         LLM Stress Test Results - 2025-08-05 21:42:34          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 5                        │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 76.64 seconds            │
│ Min Response Time                 │ 0.87 seconds             │
│ Max Response Time                 │ 4.13 seconds             │
│ Average Response Time             │ 3.75 seconds             │
│ Median Response Time              │ 3.96 seconds             │
│ P90 Response Time                 │ 4.12 seconds             │
│ P95 Response Time                 │ 4.13 seconds             │
│ P99 Response Time                 │ 4.13 seconds             │
│ Std Dev Response Time             │ 0.69 seconds             │
│ Theoretical Max Throughput        │ 24.19 requests/second    │
│ Actual Throughput                 │ 1.30 requests/second     │
│ Total Completion Tokens           │ 24207                    │
│ Total Prompt Tokens               │ 2260                     │
│ Total Tokens                      │ 26467                    │
│ Completion Tokens Per Second      │ 315.84                   │
│ Avg Completion Tokens Per Request │ 242.07                   │
│ Peak Requests In Flight           │ 5                        │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
Sure! Here's a simple way to explain **technical debt** to a non-technical
person:

---

**Imagine you're building a house.** You have a budget, a timeline, and a 
clear plan. But to save time and mone...
(myenv) root@Llm-test:/home# 

(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 10
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 10
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 40.80 seconds
         LLM Stress Test Results - 2025-08-05 21:43:54          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 10                       │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 40.80 seconds            │
│ Min Response Time                 │ 0.85 seconds             │
│ Max Response Time                 │ 4.34 seconds             │
│ Average Response Time             │ 3.90 seconds             │
│ Median Response Time              │ 4.24 seconds             │
│ P90 Response Time                 │ 4.26 seconds             │
│ P95 Response Time                 │ 4.26 seconds             │
│ P99 Response Time                 │ 4.34 seconds             │
│ Std Dev Response Time             │ 0.85 seconds             │
│ Theoretical Max Throughput        │ 23.05 requests/second    │
│ Actual Throughput                 │ 2.45 requests/second     │
│ Total Completion Tokens           │ 23552                    │
│ Total Prompt Tokens               │ 2240                     │
│ Total Tokens                      │ 25792                    │
│ Completion Tokens Per Second      │ 577.29                   │
│ Avg Completion Tokens Per Request │ 235.52                   │
│ Peak Requests In Flight           │ 10                       │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
Containers and virtual machines (VMs) are both technologies used to 
isolate and run applications, but they differ significantly in how they 
achieve this isolation and how they operate. Here's a breakd...

(myenv) root@Llm-test:/home# ./qwen3_openai_stress_test.py --concurrent 10
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/llm/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 10
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 37.97 seconds
         LLM Stress Test Results - 2025-08-05 21:47:48          
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1 │
│ Model                             │ /home/llm/Qwen3-8B       │
│ Framework                         │ auto                     │
│ Max Tokens                        │ 256                      │
│ Temperature                       │ 0.7                      │
│ Thinking Mode                     │ Default                  │
│ Concurrent Requests               │ 10                       │
│ Total Requests                    │ 100                      │
│ Successful Requests               │ 100 (100.0%)             │
│ Failed Requests                   │ 0 (0.0%)                 │
│ Total Test Duration               │ 37.97 seconds            │
│ Min Response Time                 │ 1.01 seconds             │
│ Max Response Time                 │ 4.08 seconds             │
│ Average Response Time             │ 3.59 seconds             │
│ Median Response Time              │ 3.78 seconds             │
│ P90 Response Time                 │ 3.81 seconds             │
│ P95 Response Time                 │ 3.87 seconds             │
│ P99 Response Time                 │ 4.08 seconds             │
│ Std Dev Response Time             │ 0.63 seconds             │
│ Theoretical Max Throughput        │ 24.51 requests/second    │
│ Actual Throughput                 │ 2.63 requests/second     │
│ Total Completion Tokens           │ 24342                    │
│ Total Prompt Tokens               │ 2208                     │
│ Total Tokens                      │ 26550                    │
│ Completion Tokens Per Second      │ 641.07                   │
│ Avg Completion Tokens Per Request │ 243.42                   │
│ Peak Requests In Flight           │ 10                       │
└───────────────────────────────────┴──────────────────────────┘

Sample Responses:
Sample without Thinking:
**Authentication** and **authorization** are two distinct but related 
concepts in cybersecurity and access control. Here's a clear breakdown of 
the difference:

---

### 🔐 **Authentication**  
**Defin...
```



```
 - numpy==2.2.6
 + numpy==2.3.2
 - transformers==4.54.1
 + transformers==4.53.3
```



## 0.10.1.1 vs 0.85

测试 10个并发

### 0.10.1.1

```
Starting LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/vllm/llm/Qwen/Qwen3-8B
Max Tokens: 256
Temperature: 0.7
Concurrent requests: 10
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 44.15 seconds
        LLM Stress Test Results - 2025-09-02 16:26:59        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-8B │
│ Max Tokens                 │ 256                          │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 44.14 seconds                │
│ Min Response Time          │ 1.21 seconds                 │
│ Max Response Time          │ 4.48 seconds                 │
│ Average Response Time      │ 3.96 seconds                 │
│ Median Response Time       │ 4.36 seconds                 │
│ P90 Response Time          │ 4.47 seconds                 │
│ P95 Response Time          │ 4.47 seconds                 │
│ P99 Response Time          │ 4.48 seconds                 │
│ Std Dev Response Time      │ 0.92 seconds                 │
│ Theoretical Max Throughput │ 22.34 requests/second        │
│ Actual Throughput          │ 2.27 requests/second         │
│ Total Generated Tokens     │ 16149                        │
│ Tokens Per Second          │ 365.82                       │
│ Avg Tokens Per Request     │ 161.49                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘


Test completed in 44.05 seconds
        LLM Stress Test Results - 2025-09-02 16:29:02        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-8B │
│ Max Tokens                 │ 256                          │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 10                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 44.05 seconds                │
│ Min Response Time          │ 1.05 seconds                 │
│ Max Response Time          │ 4.47 seconds                 │
│ Average Response Time      │ 3.90 seconds                 │
│ Median Response Time       │ 4.35 seconds                 │
│ P90 Response Time          │ 4.47 seconds                 │
│ P95 Response Time          │ 4.47 seconds                 │
│ P99 Response Time          │ 4.47 seconds                 │
│ Std Dev Response Time      │ 0.98 seconds                 │
│ Theoretical Max Throughput │ 22.35 requests/second        │
│ Actual Throughput          │ 2.27 requests/second         │
│ Total Generated Tokens     │ 16077                        │
│ Tokens Per Second          │ 364.96                       │
│ Avg Tokens Per Request     │ 160.77                       │
│ Peak Requests In Flight    │ 10                           │
└────────────────────────────┴──────────────────────────────┘

只有当20个并发才好

Test completed in 24.80 seconds
        LLM Stress Test Results - 2025-09-02 18:16:35        
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1     │
│ Model                      │ /home/vllm/llm/Qwen/Qwen3-8B │
│ Max Tokens                 │ 256                          │
│ Temperature                │ 0.7                          │
│ Concurrent Requests        │ 20                           │
│ Total Requests             │ 100                          │
│ Successful Requests        │ 100 (100.0%)                 │
│ Failed Requests            │ 0 (0.0%)                     │
│ Total Test Duration        │ 24.80 seconds                │
│ Min Response Time          │ 1.32 seconds                 │
│ Max Response Time          │ 5.20 seconds                 │
│ Average Response Time      │ 4.33 seconds                 │
│ Median Response Time       │ 4.89 seconds                 │
│ P90 Response Time          │ 5.09 seconds                 │
│ P95 Response Time          │ 5.09 seconds                 │
│ P99 Response Time          │ 5.20 seconds                 │
│ Std Dev Response Time      │ 1.15 seconds                 │
│ Theoretical Max Throughput │ 19.22 requests/second        │
│ Actual Throughput          │ 4.03 requests/second         │
│ Total Generated Tokens     │ 15636                        │
│ Tokens Per Second          │ 630.44                       │
│ Avg Tokens Per Request     │ 156.36                       │
│ Peak Requests In Flight    │ 20                           │
└────────────────────────────┴──────────────────────────────┘
```

### 0.85

````
Test completed in 38.16 seconds
      LLM Stress Test Results - 2025-09-02 16:30:26      
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1 │
│ Model                      │ /home/llm/Qwen3-8B       │
│ Max Tokens                 │ 256                      │
│ Temperature                │ 0.7                      │
│ Concurrent Requests        │ 10                       │
│ Total Requests             │ 100                      │
│ Successful Requests        │ 100 (100.0%)             │
│ Failed Requests            │ 0 (0.0%)                 │
│ Total Test Duration        │ 38.16 seconds            │
│ Min Response Time          │ 0.86 seconds             │
│ Max Response Time          │ 4.03 seconds             │
│ Average Response Time      │ 3.55 seconds             │
│ Median Response Time       │ 3.78 seconds             │
│ P90 Response Time          │ 3.82 seconds             │
│ P95 Response Time          │ 3.82 seconds             │
│ P99 Response Time          │ 4.03 seconds             │
│ Std Dev Response Time      │ 0.72 seconds             │
│ Theoretical Max Throughput │ 24.84 requests/second    │
│ Actual Throughput          │ 2.62 requests/second     │
│ Total Generated Tokens     │ 17157                    │
│ Tokens Per Second          │ 449.59                   │
│ Avg Tokens Per Request     │ 171.57                   │
│ Peak Requests In Flight    │ 10                       │
└────────────────────────────┴──────────────────────────┘


Test completed in 37.81 seconds
      LLM Stress Test Results - 2025-09-02 18:18:35      
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1 │
│ Model                      │ /home/llm/Qwen3-8B       │
│ Max Tokens                 │ 256                      │
│ Temperature                │ 0.7                      │
│ Concurrent Requests        │ 20                       │
│ Total Requests             │ 100                      │
│ Successful Requests        │ 100 (100.0%)             │
│ Failed Requests            │ 0 (0.0%)                 │
│ Total Test Duration        │ 37.81 seconds            │
│ Min Response Time          │ 1.31 seconds             │
│ Max Response Time          │ 7.58 seconds             │
│ Average Response Time      │ 5.18 seconds             │
│ Median Response Time       │ 3.86 seconds             │
│ P90 Response Time          │ 7.51 seconds             │
│ P95 Response Time          │ 7.54 seconds             │
│ P99 Response Time          │ 7.58 seconds             │
│ Std Dev Response Time      │ 1.97 seconds             │
│ Theoretical Max Throughput │ 13.19 requests/second    │
│ Actual Throughput          │ 2.65 requests/second     │
│ Total Generated Tokens     │ 16567                    │
│ Tokens Per Second          │ 438.21                   │
│ Avg Tokens Per Request     │ 165.67                   │
│ Peak Requests In Flight    │ 20                       │
└────────────────────────────┴──────────────────────────┘

Test completed in 38.09 seconds
      LLM Stress Test Results - 2025-09-02 18:23:56      
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                     ┃ Value                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                   │ http://localhost:8000/v1 │
│ Model                      │ /home/llm/Qwen3-8B       │
│ Max Tokens                 │ 256                      │
│ Temperature                │ 0.7                      │
│ Concurrent Requests        │ 20                       │
│ Total Requests             │ 100                      │
│ Successful Requests        │ 100 (100.0%)             │
│ Failed Requests            │ 0 (0.0%)                 │
│ Total Test Duration        │ 38.09 seconds            │
│ Min Response Time          │ 0.89 seconds             │
│ Max Response Time          │ 7.62 seconds             │
│ Average Response Time      │ 5.38 seconds             │
│ Median Response Time       │ 4.31 seconds             │
│ P90 Response Time          │ 7.61 seconds             │
│ P95 Response Time          │ 7.62 seconds             │
│ P99 Response Time          │ 7.62 seconds             │
│ Std Dev Response Time      │ 1.98 seconds             │
│ Theoretical Max Throughput │ 13.12 requests/second    │
│ Actual Throughput          │ 2.63 requests/second     │
│ Total Generated Tokens     │ 17286                    │
│ Tokens Per Second          │ 453.81                   │
│ Avg Tokens Per Request     │ 172.86                   │
│ Peak Requests In Flight    │ 20                       │
└────────────────────────────┴──────────────────────────┘
````



# L20

```
(vllm_env) vllm@iZ2ze51uio4ous9jmstk1gZ:~$ python qwen3_openai_stress_test.py --concurrent 20
\Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/vllm/llm/Qwen/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 20
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 15.75 seconds
           LLM Stress Test Results - 2025-09-04 18:36:24            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1     │
│ Model                             │ /home/vllm/llm/Qwen/Qwen3-8B │
│ Framework                         │ auto                         │
│ Max Tokens                        │ 256                          │
│ Temperature                       │ 0.7                          │
│ Thinking Mode                     │ Default                      │
│ Concurrent Requests               │ 20                           │
│ Total Requests                    │ 100                          │
│ Successful Requests               │ 100 (100.0%)                 │
│ Failed Requests                   │ 0 (0.0%)                     │
│ Total Test Duration               │ 15.75 seconds                │
│ Min Response Time                 │ 0.64 seconds                 │
│ Max Response Time                 │ 3.31 seconds                 │
│ Average Response Time             │ 2.91 seconds                 │
│ Median Response Time              │ 3.15 seconds                 │
│ P90 Response Time                 │ 3.22 seconds                 │
│ P95 Response Time                 │ 3.22 seconds                 │
│ P99 Response Time                 │ 3.31 seconds                 │
│ Std Dev Response Time             │ 0.65 seconds                 │
│ Theoretical Max Throughput        │ 30.20 requests/second        │
│ Actual Throughput                 │ 6.35 requests/second         │
│ Total Completion Tokens           │ 23693                        │
│ Total Prompt Tokens               │ 2209                         │
│ Total Tokens                      │ 25902                        │
│ Completion Tokens Per Second      │ 1504.78                      │
│ Avg Completion Tokens Per Request │ 236.93                       │
│ Peak Requests In Flight           │ 20                           │
└───────────────────────────────────┴──────────────────────────────┘

Sample Responses:
Sample without Thinking:
Load balancing is a critical technique used in web applications to distribute incoming network traffic across multiple servers or instances. Its primary goal is to optimize resource use, maximize thro...
(vllm_env) vllm@iZ2ze51uio4ous9jmstk1gZ:~$ python qwen3_openai_stress_test.py --concurrent 10
Starting Enhanced LLM Stress Test
API Base: http://localhost:8000/v1
Model: /home/vllm/llm/Qwen/Qwen3-8B
Framework: auto
Max Tokens: 256
Temperature: 0.7
Thinking Mode: Default
Concurrent requests: 10
Total requests: 100
Processing requests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Test completed in 28.09 seconds
           LLM Stress Test Results - 2025-09-04 18:37:10            
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Metric                            ┃ Value                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ API Base                          │ http://localhost:8000/v1     │
│ Model                             │ /home/vllm/llm/Qwen/Qwen3-8B │
│ Framework                         │ auto                         │
│ Max Tokens                        │ 256                          │
│ Temperature                       │ 0.7                          │
│ Thinking Mode                     │ Default                      │
│ Concurrent Requests               │ 10                           │
│ Total Requests                    │ 100                          │
│ Successful Requests               │ 100 (100.0%)                 │
│ Failed Requests                   │ 0 (0.0%)                     │
│ Total Test Duration               │ 28.09 seconds                │
│ Min Response Time                 │ 0.82 seconds                 │
│ Max Response Time                 │ 2.90 seconds                 │
│ Average Response Time             │ 2.71 seconds                 │
│ Median Response Time              │ 2.80 seconds                 │
│ P90 Response Time                 │ 2.82 seconds                 │
│ P95 Response Time                 │ 2.82 seconds                 │
│ P99 Response Time                 │ 2.90 seconds                 │
│ Std Dev Response Time             │ 0.33 seconds                 │
│ Theoretical Max Throughput        │ 34.43 requests/second        │
│ Actual Throughput                 │ 3.56 requests/second         │
│ Total Completion Tokens           │ 24820                        │
│ Total Prompt Tokens               │ 2234                         │
│ Total Tokens                      │ 27054                        │
│ Completion Tokens Per Second      │ 883.52                       │
│ Avg Completion Tokens Per Request │ 248.20                       │
│ Peak Requests In Flight           │ 10                           │
└───────────────────────────────────┴──────────────────────────────┘

Sample Responses:
Sample without Thinking:
REST (Representational State Transfer) is an architectural style for designing networked applications, particularly web services. REST API design is based on a set of principles that guide how web ser...
(vllm_env) vllm@iZ2ze51uio4ous9jmstk1gZ:~$ 
```
