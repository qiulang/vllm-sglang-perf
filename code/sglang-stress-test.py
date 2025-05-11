#!/usr/bin/env python3
"""
SGLang Stress Test Script

This script performs stress testing on SGLang by sending multiple concurrent requests
and measuring response times and throughput with accurate calculations.
"""

import argparse
import asyncio
import aiohttp
import json
import time
import statistics
import sys
import random
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, TaskID

# Default values
DEFAULT_URL = "http://localhost:30000/generate"
DEFAULT_CONCURRENT = 5
DEFAULT_TOTAL = 20
DEFAULT_TIMEOUT = 120  # 2 minutes timeout
DEFAULT_MAX_TOKENS = 256

# List of diverse prompts to prevent caching
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
    "Explain how public key cryptography works in simple terms."
]

console = Console()


async def send_request(session, url, request_id, progress_bar, task_id, max_tokens=DEFAULT_MAX_TOKENS):
    """Send a single request to SGLang and measure the response time."""
    start_time = time.time()
    prompt = random.choice(PROMPT_LIST)

    # Format for SGLang API - using the simplified format
    data = {
        "text": prompt,
        "max_tokens": max_tokens
    }

    # Set proper headers
    headers = {
        "Content-Type": "application/json"
    }

    try:
        async with session.post(url, json=data, headers=headers, timeout=DEFAULT_TIMEOUT) as response:
            elapsed_time = time.time() - start_time
            progress_bar.update(task_id, advance=1)

            if response.status == 200:
                result = await response.json()

                # Extract text from SGLang response
                # Adjust this based on your SGLang response format
                response_text = result.get("text", "")
                tokens = len(response_text.split())

                return {
                    "request_id": request_id,
                    "status": response.status,
                    "elapsed_time": elapsed_time,
                    "tokens": tokens,
                    "tokens_per_second": tokens / elapsed_time if elapsed_time > 0 else 0,
                    "response_text": response_text[:50] + "..." if len(response_text) > 50 else response_text,
                    "start_time": start_time,
                    "end_time": time.time()
                }
            else:
                error_text = await response.text()
                return {
                    "request_id": request_id,
                    "status": response.status,
                    "error": error_text,
                    "elapsed_time": elapsed_time,
                    "start_time": start_time,
                    "end_time": time.time()
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
            "end_time": time.time()
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
            "end_time": time.time()
        }


async def run_stress_test(url, concurrent_requests, total_requests, max_tokens=DEFAULT_MAX_TOKENS):
    """Run the stress test with the specified parameters."""
    results = []
    overall_start_time = time.time()

    connector = aiohttp.TCPConnector(limit=concurrent_requests)

    with Progress() as progress:
        task_id = progress.add_task(
            "[cyan]Processing requests...", total=total_requests)

        async with aiohttp.ClientSession(connector=connector) as session:
            # Create a list of tasks for all requests
            tasks = []
            for i in range(total_requests):
                tasks.append(send_request(
                    session, url, i+1, progress, task_id, max_tokens=max_tokens
                ))

            # Process requests in batches of concurrent_requests
            for i in range(0, len(tasks), concurrent_requests):
                batch = tasks[i:i+concurrent_requests]
                batch_results = await asyncio.gather(*batch)
                results.extend(batch_results)

    overall_end_time = time.time()
    overall_duration = overall_end_time - overall_start_time

    # Add overall test timing information
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


def print_results(results, test_info, concurrent_requests, total_requests, url, max_tokens):
    """Print the test results in a formatted table with improved metrics."""
    # Calculate statistics
    successful_requests = [r for r in results if isinstance(
        r.get("status"), int) and r.get("status") == 200]
    failed_requests = [r for r in results if r not in successful_requests]

    if not successful_requests:
        console.print("[bold red]No successful requests![/bold red]")
        return

    response_times = [r["elapsed_time"] for r in successful_requests]

    # Calculate percentiles for response times
    response_percentiles = calculate_percentiles(response_times)

    # Create and display the statistics table
    stats_table = Table(
        title=f"SGLang Stress Test Results - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    stats_table.add_column("Metric", style="cyan")
    stats_table.add_column("Value", style="green")

    stats_table.add_row("URL", url)
    stats_table.add_row("Max Tokens", str(max_tokens))
    stats_table.add_row("Concurrent Requests", str(concurrent_requests))
    stats_table.add_row("Total Requests", str(total_requests))
    stats_table.add_row("Successful Requests",
                        f"{len(successful_requests)} ({len(successful_requests)/total_requests*100:.1f}%)")
    stats_table.add_row(
        "Failed Requests", f"{len(failed_requests)} ({len(failed_requests)/total_requests*100:.1f}%)")
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

        # Calculate throughput - both ways
        # 1. Traditional (but misleading for multi-batch) method
        max_elapsed = max([r["elapsed_time"] for r in results])
        traditional_throughput = len(successful_requests) / max_elapsed

        # 2. Actual end-to-end throughput
        actual_throughput = len(successful_requests) / \
            test_info["overall_duration"]

        stats_table.add_row("Theoretical Max Throughput",
                            f"{traditional_throughput:.2f} requests/second")
        stats_table.add_row("Actual Throughput",
                            f"{actual_throughput:.2f} requests/second")

        # Calculate tokens per second if available
        total_tokens = sum([r.get("tokens", 0) for r in successful_requests])
        tokens_per_second = total_tokens / test_info["overall_duration"]
        stats_table.add_row("Total Generated Tokens", f"{total_tokens}")
        stats_table.add_row("Tokens Per Second", f"{tokens_per_second:.2f}")

        # Calculate avg tokens per request
        avg_tokens_per_request = total_tokens / len(successful_requests)
        stats_table.add_row("Avg Tokens Per Request",
                            f"{avg_tokens_per_request:.2f}")

        # Peak requests in flight
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

    # Print failed requests if any
    if failed_requests:
        failed_table = Table(title="Failed Requests")
        failed_table.add_column("Request ID", style="cyan")
        failed_table.add_column("Status", style="red")
        failed_table.add_column("Error", style="yellow")

        for req in failed_requests:
            failed_table.add_row(
                str(req.get("request_id", "N/A")),
                str(req.get("status", "N/A")),
                str(req.get("error", "Unknown error"))
            )

        console.print(failed_table)

    # Print sample response
    if successful_requests:
        console.print("\n[bold cyan]Sample Response:[/bold cyan]")
        sample_response = successful_requests[0].get("response_text", "")
        console.print(f"[green]{sample_response}[/green]")


def main():
    parser = argparse.ArgumentParser(description="SGLang Stress Test Tool")
    parser.add_argument("--url", default=DEFAULT_URL,
                        help=f"SGLang API URL (default: {DEFAULT_URL})")
    parser.add_argument("--concurrent", type=int, default=DEFAULT_CONCURRENT,
                        help=f"Number of concurrent requests (default: {DEFAULT_CONCURRENT})")
    parser.add_argument("--total", type=int, default=DEFAULT_TOTAL,
                        help=f"Total number of requests to send (default: {DEFAULT_TOTAL})")
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS,
                        help=f"Maximum tokens to generate (default: {DEFAULT_MAX_TOKENS})")

    args = parser.parse_args()

    console.print(f"[bold green]Starting SGLang Stress Test[/bold green]")
    console.print(f"URL: {args.url}")
    console.print(f"Max Tokens: {args.max_tokens}")
    console.print(f"Concurrent requests: {args.concurrent}")
    console.print(f"Total requests: {args.total}")

    start_time = time.time()

    try:
        results, test_info = asyncio.run(run_stress_test(
            args.url,
            args.concurrent,
            args.total,
            args.max_tokens
        ))

        total_time = time.time() - start_time
        console.print(
            f"[bold green]Test completed in {total_time:.2f} seconds[/bold green]")

        print_results(
            results,
            test_info,
            args.concurrent,
            args.total,
            args.url,
            args.max_tokens
        )

    except KeyboardInterrupt:
        console.print("[bold red]Test interrupted by user[/bold red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Error running test: {str(e)}[/bold red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
