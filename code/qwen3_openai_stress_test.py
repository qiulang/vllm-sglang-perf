#!/usr/bin/env python3
"""
Enhanced LLM Stress Test Script (OpenAI API Compatible)

Features:
- Explicit thinking mode control
- Accurate token counting from API response
- Thinking mode detection and analysis
- Detailed performance metrics
- Framework-agnostic testing

Supports:
- vLLM with OpenAI API
- SGLang with OpenAI API
- Any OpenAI-compatible inference server
"""

import argparse
import asyncio
import time
import statistics
import sys
import os
import random
import json
from datetime import datetime
from openai import AsyncOpenAI
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, TaskID

# Default values
DEFAULT_API_BASE = "http://localhost:8000/v1"
DEFAULT_API_KEY = "not-needed"
DEFAULT_MODEL = "qwen3-14b"
DEFAULT_CONCURRENT = 10
DEFAULT_TOTAL = 100
DEFAULT_TIMEOUT = 120
DEFAULT_MAX_TOKENS = 256
DEFAULT_TEMPERATURE = 0.7

# Diverse prompts to prevent caching and test various reasoning scenarios
PROMPT_LIST = [
    "Explain what makes a good API in one paragraph.",
    "What are three key considerations when designing a distributed system?",
    "Write a short poem about artificial intelligence.",
    "Describe the concept of technical debt to a non-technical person.",
    "What are the main differences between SQL and NoSQL databases?",
    "Explain the CAP theorem in simple terms.",
    "What are some best practices for securing a web application?",
    "Describe how virtualization works in cloud computing.",
    "What is the difference between supervised and unsupervised machine learning?",
    "Explain how public key cryptography works in simple terms.",
    "What are the advantages and disadvantages of microservices architecture?",
    "How does HTTP caching improve web performance?",
    "Explain the concept of eventual consistency in distributed systems.",
    "What is the difference between authentication and authorization?",
    "Describe how DNS resolution works step by step.",
    "What are the main principles of REST API design?",
    "Explain how load balancing works in web applications.",
    "What is the purpose of a CDN and how does it work?",
    "Describe the difference between horizontal and vertical scaling.",
    "How do containers differ from virtual machines?"
]

console = Console()


def extract_thinking_content(response_text):
    """Extract thinking content from response if present."""
    if "<think>" in response_text and "</think>" in response_text:
        try:
            start_idx = response_text.index("<think>") + len("<think>")
            end_idx = response_text.index("</think>")
            thinking_content = response_text[start_idx:end_idx].strip()

            # Extract final answer (content after </think>)
            final_answer = response_text[end_idx + len("</think>"):].strip()

            return {
                "has_thinking": True,
                "thinking_content": thinking_content,
                "final_answer": final_answer,
                "thinking_words": len(thinking_content.split()),
                "final_words": len(final_answer.split())
            }
        except (ValueError, IndexError):
            return {
                "has_thinking": False,
                "thinking_content": "",
                "final_answer": response_text,
                "thinking_words": 0,
                "final_words": len(response_text.split())
            }
    else:
        return {
            "has_thinking": False,
            "thinking_content": "",
            "final_answer": response_text,
            "thinking_words": 0,
            "final_words": len(response_text.split())
        }


async def send_request(client, model, request_id, progress_bar, task_id,
                       max_tokens=DEFAULT_MAX_TOKENS, temperature=DEFAULT_TEMPERATURE,
                       enable_thinking=None, framework="auto"):
    """Send a single request to the LLM server and measure the response time."""
    start_time = time.time()
    prompt = random.choice(PROMPT_LIST)

    # Prepare extra parameters for thinking mode control
    extra_body = {}
    if enable_thinking is not None:
        if framework.lower() in ["vllm", "auto"]:
            # vLLM parameter format
            extra_body["chat_template_kwargs"] = {
                "enable_thinking": enable_thinking}
        elif framework.lower() == "sglang":
            # SGLang might use different parameter format - adjust as needed
            extra_body["chat_template_kwargs"] = {
                "enable_thinking": enable_thinking}

    try:
        # Using ChatCompletions API
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            timeout=DEFAULT_TIMEOUT,
            **({"extra_body": extra_body} if extra_body else {})
        )

        elapsed_time = time.time() - start_time
        progress_bar.update(task_id, advance=1)

        # Extract response content and analyze thinking
        response_text = response.choices[0].message.content
        thinking_analysis = extract_thinking_content(response_text)

        # Get accurate token counts from API response
        usage = response.usage if hasattr(
            response, 'usage') and response.usage else None
        completion_tokens = usage.completion_tokens if usage else len(
            response_text.split())
        prompt_tokens = usage.prompt_tokens if usage else len(prompt.split())
        total_tokens = usage.total_tokens if usage else (
            completion_tokens + prompt_tokens)

        return {
            "request_id": request_id,
            "status": 200,
            "elapsed_time": elapsed_time,
            "prompt": prompt,
            "response_text": response_text,
            "completion_tokens": completion_tokens,
            "prompt_tokens": prompt_tokens,
            "total_tokens": total_tokens,
            "tokens_per_second": completion_tokens / elapsed_time if elapsed_time > 0 else 0,
            "start_time": start_time,
            "end_time": time.time(),
            "enable_thinking": enable_thinking,
            **thinking_analysis
        }

    except asyncio.TimeoutError:
        elapsed_time = time.time() - start_time
        progress_bar.update(task_id, advance=1)
        return {
            "request_id": request_id,
            "status": "timeout",
            "error": f"Request timed out after {elapsed_time:.2f} seconds",
            "elapsed_time": elapsed_time,
            "start_time": start_time,
            "end_time": time.time(),
            "enable_thinking": enable_thinking
        }
    except Exception as e:
        elapsed_time = time.time() - start_time
        progress_bar.update(task_id, advance=1)
        return {
            "request_id": request_id,
            "status": "error",
            "error": str(e),
            "elapsed_time": elapsed_time,
            "start_time": start_time,
            "end_time": time.time(),
            "enable_thinking": enable_thinking
        }


async def run_stress_test(api_base, api_key, model, concurrent_requests, total_requests,
                          max_tokens=DEFAULT_MAX_TOKENS, temperature=DEFAULT_TEMPERATURE,
                          enable_thinking=None, framework="auto"):
    """Run the stress test with the specified parameters."""
    results = []
    overall_start_time = time.time()

    # Create OpenAI client
    client = AsyncOpenAI(
        base_url=api_base,
        api_key=api_key
    )

    with Progress() as progress:
        task_id = progress.add_task(
            "[cyan]Processing requests...", total=total_requests)

        # Create semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(concurrent_requests)

        async def bounded_request(request_id):
            async with semaphore:
                return await send_request(
                    client, model, request_id, progress, task_id,
                    max_tokens=max_tokens, temperature=temperature,
                    enable_thinking=enable_thinking, framework=framework
                )

        # Create tasks for all requests
        tasks = [bounded_request(i+1) for i in range(total_requests)]

        # Execute all tasks concurrently (but bounded by semaphore)
        results = await asyncio.gather(*tasks)

    overall_end_time = time.time()
    overall_duration = overall_end_time - overall_start_time

    test_info = {
        "overall_start_time": overall_start_time,
        "overall_end_time": overall_end_time,
        "overall_duration": overall_duration
    }

    return results, test_info


def calculate_percentiles(values, percentiles=[50, 90, 95, 99]):
    """Calculate percentiles from a list of values."""
    if not values:
        return {f"p{p}": 0 for p in percentiles}

    sorted_values = sorted(values)
    result = {}
    for p in percentiles:
        idx = int(len(sorted_values) * p / 100)
        if idx >= len(sorted_values):
            idx = len(sorted_values) - 1
        result[f"p{p}"] = sorted_values[idx]
    return result


def analyze_thinking_mode_results(results):
    """Analyze thinking mode specific metrics."""
    successful_requests = [r for r in results if r.get("status") == 200]
    if not successful_requests:
        return {}

    thinking_requests = [
        r for r in successful_requests if r.get("has_thinking", False)]
    non_thinking_requests = [
        r for r in successful_requests if not r.get("has_thinking", False)]

    analysis = {
        "total_requests": len(successful_requests),
        "thinking_requests": len(thinking_requests),
        "non_thinking_requests": len(non_thinking_requests),
        "thinking_percentage": len(thinking_requests) / len(successful_requests) * 100 if successful_requests else 0
    }

    if thinking_requests:
        thinking_words = [r.get("thinking_words", 0)
                          for r in thinking_requests]
        final_words = [r.get("final_words", 0) for r in thinking_requests]
        thinking_times = [r["elapsed_time"] for r in thinking_requests]

        analysis.update({
            "avg_thinking_words": statistics.mean(thinking_words),
            "avg_final_words": statistics.mean(final_words),
            "avg_thinking_response_time": statistics.mean(thinking_times),
            "thinking_tokens_per_second": statistics.mean([r["tokens_per_second"] for r in thinking_requests])
        })

    if non_thinking_requests:
        non_thinking_times = [r["elapsed_time"] for r in non_thinking_requests]
        analysis.update({
            "avg_non_thinking_response_time": statistics.mean(non_thinking_times),
            "non_thinking_tokens_per_second": statistics.mean([r["tokens_per_second"] for r in non_thinking_requests])
        })

    return analysis


def print_results(results, test_info, concurrent_requests, total_requests, model, api_base,
                  max_tokens, temperature, enable_thinking, framework):
    """Print comprehensive test results."""
    # Calculate basic statistics
    successful_requests = [r for r in results if r.get("status") == 200]
    failed_requests = [r for r in results if r not in successful_requests]

    if not successful_requests:
        console.print("[bold red]No successful requests![/bold red]")
        return

    response_times = [r["elapsed_time"] for r in successful_requests]
    completion_tokens = [r.get("completion_tokens", 0)
                         for r in successful_requests]

    # Calculate percentiles
    response_percentiles = calculate_percentiles(response_times)

    # Create main statistics table
    stats_table = Table(
        title=f"LLM Stress Test Results - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    stats_table.add_column("Metric", style="cyan")
    stats_table.add_column("Value", style="green")

    # Basic configuration
    stats_table.add_row("API Base", api_base)
    stats_table.add_row("Model", model)
    stats_table.add_row("Framework", framework)
    stats_table.add_row("Max Tokens", str(max_tokens))
    stats_table.add_row("Temperature", str(temperature))
    stats_table.add_row("Thinking Mode", str(enable_thinking)
                        if enable_thinking is not None else "Default")

    # Request statistics
    stats_table.add_row("Concurrent Requests", str(concurrent_requests))
    stats_table.add_row("Total Requests", str(total_requests))
    stats_table.add_row("Successful Requests",
                        f"{len(successful_requests)} ({len(successful_requests)/total_requests*100:.1f}%)")
    stats_table.add_row("Failed Requests",
                        f"{len(failed_requests)} ({len(failed_requests)/total_requests*100:.1f}%)")

    # Timing statistics
    stats_table.add_row("Total Test Duration",
                        f"{test_info['overall_duration']:.2f} seconds")

    if response_times:
        stats_table.add_row("Min Response Time",
                            f"{min(response_times):.2f} seconds")
        stats_table.add_row("Max Response Time",
                            f"{max(response_times):.2f} seconds")
        stats_table.add_row("Average Response Time",
                            f"{statistics.mean(response_times):.2f} seconds")
        stats_table.add_row("Median Response Time",
                            f"{statistics.median(response_times):.2f} seconds")
        stats_table.add_row("P90 Response Time",
                            f"{response_percentiles['p90']:.2f} seconds")
        stats_table.add_row("P95 Response Time",
                            f"{response_percentiles['p95']:.2f} seconds")
        stats_table.add_row("P99 Response Time",
                            f"{response_percentiles['p99']:.2f} seconds")

        if len(response_times) > 1:
            stats_table.add_row("Std Dev Response Time",
                                f"{statistics.stdev(response_times):.2f} seconds")

        # Throughput calculations
        actual_throughput = len(successful_requests) / \
            test_info["overall_duration"]
        theoretical_throughput = len(
            successful_requests) / max(response_times) if response_times else 0

        stats_table.add_row("Theoretical Max Throughput",
                            f"{theoretical_throughput:.2f} requests/second")
        stats_table.add_row("Actual Throughput",
                            f"{actual_throughput:.2f} requests/second")

        # Token statistics
        total_completion_tokens = sum(completion_tokens)
        total_prompt_tokens = sum([r.get("prompt_tokens", 0)
                                  for r in successful_requests])
        total_tokens = sum([r.get("total_tokens", 0)
                           for r in successful_requests])

        tokens_per_second = total_completion_tokens / \
            test_info["overall_duration"]
        avg_completion_tokens = statistics.mean(completion_tokens)

        stats_table.add_row("Total Completion Tokens",
                            f"{total_completion_tokens}")
        stats_table.add_row("Total Prompt Tokens", f"{total_prompt_tokens}")
        stats_table.add_row("Total Tokens", f"{total_tokens}")
        stats_table.add_row("Completion Tokens Per Second",
                            f"{tokens_per_second:.2f}")
        stats_table.add_row("Avg Completion Tokens Per Request",
                            f"{avg_completion_tokens:.2f}")

        # Concurrency analysis
        all_times = [(r["start_time"], "start")
                     for r in results] + [(r["end_time"], "end") for r in results]
        all_times.sort()

        max_concurrent = 0
        current_concurrent = 0
        for _, event_type in all_times:
            if event_type == "start":
                current_concurrent += 1
            else:
                current_concurrent -= 1
            max_concurrent = max(max_concurrent, current_concurrent)

        stats_table.add_row("Peak Requests In Flight", str(max_concurrent))

    console.print(stats_table)

    # Thinking mode analysis
    thinking_analysis = analyze_thinking_mode_results(results)
    if thinking_analysis and thinking_analysis["thinking_requests"] > 0:
        thinking_table = Table(title="Thinking Mode Analysis")
        thinking_table.add_column("Metric", style="cyan")
        thinking_table.add_column("Value", style="yellow")

        thinking_table.add_row("Requests with Thinking",
                               f"{thinking_analysis['thinking_requests']}")
        thinking_table.add_row("Requests without Thinking",
                               f"{thinking_analysis['non_thinking_requests']}")
        thinking_table.add_row(
            "Thinking Percentage", f"{thinking_analysis['thinking_percentage']:.1f}%")

        if "avg_thinking_words" in thinking_analysis:
            thinking_table.add_row(
                "Avg Thinking Words", f"{thinking_analysis['avg_thinking_words']:.1f}")
            thinking_table.add_row(
                "Avg Final Answer Words", f"{thinking_analysis['avg_final_words']:.1f}")
            thinking_table.add_row(
                "Avg Thinking Response Time", f"{thinking_analysis['avg_thinking_response_time']:.2f}s")
            thinking_table.add_row(
                "Thinking Tokens/Second", f"{thinking_analysis['thinking_tokens_per_second']:.2f}")

        if "avg_non_thinking_response_time" in thinking_analysis:
            thinking_table.add_row("Avg Non-Thinking Response Time",
                                   f"{thinking_analysis['avg_non_thinking_response_time']:.2f}s")
            thinking_table.add_row(
                "Non-Thinking Tokens/Second", f"{thinking_analysis['non_thinking_tokens_per_second']:.2f}")

        console.print(thinking_table)

    # Show failed requests if any
    if failed_requests:
        failed_table = Table(title="Failed Requests")
        failed_table.add_column("Request ID", style="cyan")
        failed_table.add_column("Status", style="red")
        failed_table.add_column("Error", style="yellow")

        for req in failed_requests[:10]:  # Show first 10 failures
            failed_table.add_row(
                str(req.get("request_id", "N/A")),
                str(req.get("status", "N/A")),
                str(req.get("error", "Unknown error"))[:50]
            )

        if len(failed_requests) > 10:
            failed_table.add_row(
                "...", "...", f"... and {len(failed_requests) - 10} more failures")

        console.print(failed_table)

    # Show sample responses
    if successful_requests:
        console.print("\n[bold cyan]Sample Responses:[/bold cyan]")

        # Show thinking and non-thinking examples if available
        thinking_sample = next(
            (r for r in successful_requests if r.get("has_thinking", False)), None)
        non_thinking_sample = next(
            (r for r in successful_requests if not r.get("has_thinking", False)), None)

        if thinking_sample:
            console.print("[yellow]Sample with Thinking:[/yellow]")
            sample_text = thinking_sample["response_text"][:200] + "..." if len(
                thinking_sample["response_text"]) > 200 else thinking_sample["response_text"]
            console.print(f"[green]{sample_text}[/green]")

        if non_thinking_sample:
            console.print("[yellow]Sample without Thinking:[/yellow]")
            sample_text = non_thinking_sample["response_text"][:200] + "..." if len(
                non_thinking_sample["response_text"]) > 200 else non_thinking_sample["response_text"]
            console.print(f"[green]{sample_text}[/green]")


def main():
    parser = argparse.ArgumentParser(
        description="Enhanced LLM Stress Test Tool (OpenAI API Compatible)")
    parser.add_argument("--api-base", default=os.getenv("LLM_API_BASE", DEFAULT_API_BASE),
                        help=f"API base URL (default: {DEFAULT_API_BASE})")
    parser.add_argument("--api-key", default=os.getenv("LLM_API_KEY", DEFAULT_API_KEY),
                        help="API key (default: not-needed)")
    parser.add_argument("--model", default=os.getenv("LLM_MODEL", DEFAULT_MODEL),
                        help=f"Model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--framework", choices=["vllm", "sglang", "auto"], default="auto",
                        help="Framework type for thinking mode parameters (default: auto)")
    parser.add_argument("--concurrent", type=int, default=DEFAULT_CONCURRENT,
                        help=f"Number of concurrent requests (default: {DEFAULT_CONCURRENT})")
    parser.add_argument("--total", type=int, default=DEFAULT_TOTAL,
                        help=f"Total number of requests to send (default: {DEFAULT_TOTAL})")
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS,
                        help=f"Maximum tokens to generate (default: {DEFAULT_MAX_TOKENS})")
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE,
                        help=f"Temperature for sampling (default: {DEFAULT_TEMPERATURE})")
    parser.add_argument("--enable-thinking", type=str, choices=["true", "false"], default=None,
                        help="Explicitly enable or disable thinking mode (default: model default)")

    args = parser.parse_args()

    # Convert string to boolean for enable_thinking
    enable_thinking = None
    if args.enable_thinking is not None:
        enable_thinking = args.enable_thinking.lower() == "true"

    console.print(
        f"[bold green]Starting Enhanced LLM Stress Test[/bold green]")
    console.print(f"API Base: {args.api_base}")
    console.print(f"Model: {args.model}")
    console.print(f"Framework: {args.framework}")
    console.print(f"Max Tokens: {args.max_tokens}")
    console.print(f"Temperature: {args.temperature}")
    console.print(
        f"Thinking Mode: {enable_thinking if enable_thinking is not None else 'Default'}")
    console.print(f"Concurrent requests: {args.concurrent}")
    console.print(f"Total requests: {args.total}")

    start_time = time.time()

    try:
        results, test_info = asyncio.run(run_stress_test(
            args.api_base,
            args.api_key,
            args.model,
            args.concurrent,
            args.total,
            args.max_tokens,
            args.temperature,
            enable_thinking,
            args.framework
        ))

        total_time = time.time() - start_time
        console.print(
            f"[bold green]Test completed in {total_time:.2f} seconds[/bold green]")

        print_results(
            results, test_info, args.concurrent, args.total,
            args.model, args.api_base, args.max_tokens, args.temperature,
            enable_thinking, args.framework
        )

        # Optional: Save detailed results to JSON
        if len(sys.argv) > 1 and "--save-json" in sys.argv:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"stress_test_results_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump({
                    "test_config": {
                        "api_base": args.api_base,
                        "model": args.model,
                        "framework": args.framework,
                        "concurrent": args.concurrent,
                        "total": args.total,
                        "max_tokens": args.max_tokens,
                        "temperature": args.temperature,
                        "enable_thinking": enable_thinking
                    },
                    "test_info": test_info,
                    "results": results
                }, f, indent=2, default=str)
            console.print(f"[blue]Detailed results saved to {filename}[/blue]")

    except KeyboardInterrupt:
        console.print("[bold red]Test interrupted by user[/bold red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Error running test: {str(e)}[/bold red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
