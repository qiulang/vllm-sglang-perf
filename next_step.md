# Next Phase: GPU Performance Testing Plan

## Current Baseline

**Established Performance Baseline:**
- Hardware: Single NVIDIA A10 GPU (24GB VRAM)
- Model: Qwen-8B AWQ quantized model
- Framework: vLLM
- Performance: 10 concurrent requests with P95 = 3.81 seconds
- Status: Verified as stable across multiple test runs

## Objective

Identify how different midrange GPUs perform with the same workload, specifically determining the maximum concurrent request capacity while maintaining P95 ≤ 3.81 seconds.

## Next Target: NVIDIA L20

### Why L20?
- Midrange pricing tier (similar to A10)
- Ada Lovelace architecture (newer than A10's Ampere)
- 48GB VRAM (2x A10's capacity)
- Higher memory bandwidth: 864 GB/s vs A10's 600 GB/s
- Expected performance: 15-25 concurrent requests

### Test Configuration

**vLLM Parameters:**
```bash
vllm serve /path/to/qwen-8b-awq \
  --max-model-len 8192 \
  --tensor-parallel-size 1 \
  --gpu-memory-utilization 0.85 \
  --max-num-seqs 50
```

**Test Progression:**
1. Start at 15 concurrent requests (50% above A10 baseline)
2. Increment by 5: 20, 25, 30, 35, 40+
3. Stop when P95 consistently exceeds 3.81s
4. Run each configuration for minimum 10 minutes

## Key Metrics to Collect

### Primary Metrics
- **P95 response time** (must stay ≤ 3.81s)
- **Maximum concurrent requests** meeting the P95 target
- **P99 response time** (failure detection)
- **Actual throughput** (requests/second)

### Secondary Metrics
- VRAM utilization at peak performance
- GPU utilization percentage
- Tokens per second generation rate
- Test duration for stability verification

### Comparative Analysis
- Direct performance ratio vs A10 (concurrent request capacity)
- Memory efficiency comparison
- Cost-performance analysis (if pricing available)

## Testing Methodology

### Consistency Requirements
- **Same model**: Exact Qwen-8B AWQ version as A10 tests
- **Same request patterns**: Use identical prompt diversity and token lengths
- **Same duration**: Minimum 10-minute runs per configuration
- **Multiple runs**: At least 3 runs per configuration for consistency

### Documentation Template
For each test configuration:
```
GPU: L20
Concurrent Requests: [X]
P95 Response Time: [X.XX]s
P99 Response Time: [X.XX]s
Throughput: [X.XX] req/s
VRAM Usage: [XX]GB ([XX]%)
GPU Utilization: [XX]%
Test Duration: [XX] minutes
Status: [PASS/FAIL for P95 ≤ 3.81s]
```

## Expected Outcomes

### Performance Hypothesis
Based on architectural improvements and doubled VRAM:
- **Conservative estimate**: 15-20 concurrent requests
- **Optimistic estimate**: 20-25 concurrent requests
- **Limiting factor**: Likely compute capacity before memory limits

### Decision Points
- If L20 significantly outperforms A10: Continue with higher-end midrange GPUs
- If improvement is marginal: Focus on multi-GPU configurations
- If memory allows: Test higher context lengths (12K, 16K tokens)

## Future Testing Pipeline

### Additional Midrange GPUs
After L20 baseline:
- RTX 4090 (24GB, consumer Ada Lovelace)
- RTX 3090 (24GB, consumer Ampere)  
- A40 (48GB, professional Ampere)

### Multi-GPU Phase
For GPUs that can't meet targets alone:
- 2x GPU tensor parallelism
- 4x GPU configurations
- Scaling efficiency analysis

## Success Criteria

**Phase Complete When:**
- L20 maximum concurrent capacity determined
- P95 performance envelope mapped
- Direct A10 vs L20 comparison documented
- Cost-performance ratio calculated
- Recommendations for next GPU target identified

## Risks and Mitigations

**Potential Issues:**
- Model loading failures due to configuration differences
- Inconsistent results across runs
- Hardware availability constraints

**Mitigations:**
- Verify model loading before extended testing
- Use identical test scripts and procedures
- Run multiple validation tests before concluding