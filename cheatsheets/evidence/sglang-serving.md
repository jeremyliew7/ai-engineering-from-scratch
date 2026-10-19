# Evidence: cheatsheets/sglang-serving.md

<!-- Line numbers are estimates made from the trimmed section text. The build must resolve each one, and any reference that does not hold a fact must be corrected or removed. -->

Abbreviations: S = manuals/sglang-101/sections, C = manuals/sglang-101/capture, M = manuals/sglang-101.

## Architecture: Three processes (architecture, 5 nodes)
- Client, POST /generate: S/1-2-one-request-end-to-end.md:3
- TokenizerManager, text to ids: S/2-1-sglang-serve-and-the-three-processes.md:17
- Scheduler, batches and KV pool: S/2-2-the-scheduler-loop-and-schedule-policy.md:3
- Model forward, prefill and decode: S/2-2-the-scheduler-loop-and-schedule-policy.md:25
- Detokenizer, ids to text: S/2-1-sglang-serve-and-the-three-processes.md:17

## Flow: One request (flow, 5 steps)
1. POST /generate with a five-token prompt: S/1-2-one-request-end-to-end.md:3
2. cached_tokens 2, 3 new tokens: S/1-2-one-request-end-to-end.md:46
3. 12 tokens returned: S/1-2-one-request-end-to-end.md:40
4. finish_reason length: S/1-2-one-request-end-to-end.md:42
5. 950 ms end to end: S/1-2-one-request-end-to-end.md:3

## Start a server (annotated-code, 3 lines)
- MLX server line with --disable-cuda-graph and --mem-fraction-static 0.4: S/2-1-sglang-serve-and-the-three-processes.md:35
- GPU server line with --mem-fraction-static 0.7: S/5-1-sglang-benchmark-serving.md:110
- python3 capture/run.py --check: C/README.md:12

## Commands (command-table, 8 rows)
- sglang serve --model-path --port: S/2-1-sglang-serve-and-the-three-processes.md:35
- --enable-cache-report: S/2-1-sglang-serve-and-the-three-processes.md:42
- --enable-metrics default off: S/5-2-the-metrics-endpoint.md:9
- --mem-fraction-static: S/3-2-mem-fraction-static-and-startup-sizing.md:9
- --schedule-policy lpm: S/2-2-the-scheduler-loop-and-schedule-policy.md:44
- --kv-cache-dtype fp8_e4m3: S/4-3-quantization.md:30
- --enable-deterministic-inference: S/4-6-deterministic-inference-and-logprobs.md:9
- python3 capture/run.py --check: C/README.md:12

## Four numbers (concepts, 5)
- TTFT: S/1-1-what-a-serving-engine-owns.md:20
- TPOT: S/1-1-what-a-serving-engine-owns.md:22
- Throughput: S/1-1-what-a-serving-engine-owns.md:24
- Goodput: S/1-1-what-a-serving-engine-owns.md:26
- KV pool, max_total_num_tokens: S/3-1-kv-bytes-per-token-and-the-kv-pool.md:62

## Order of changes (flow, 5 steps)
1. Benchmark at three concurrency levels: S/7-1-operating-sglang.md:120
2. --mem-fraction-static on a shared machine: S/7-1-operating-sglang.md:122
3. Shared text first in prompts: S/7-1-operating-sglang.md:124
4. Cap --max-running-requests at the knee: S/7-1-operating-sglang.md:126
5. One flag per run, --tp-size only when weights do not fit: S/7-1-operating-sglang.md:128, S/6-1-tp-size-dp-size-and-attn-dp-size.md:3

## Defaults (defaults, 8 rows)
- --tp-size 1: S/r-1-flags-and-defaults.md:36
- --schedule-policy fcfs: S/r-1-flags-and-defaults.md:27
- --radix-eviction-policy lru: S/r-1-flags-and-defaults.md:33
- --schedule-conservativeness 1.0: S/r-1-flags-and-defaults.md:16
- --decode-log-interval 40: S/2-2-the-scheduler-loop-and-schedule-policy.md:31
- --num-reserved-decode-tokens 512: S/6-3-prefill-decode-disaggregation.md:58
- --cache-threshold 0.3: S/6-4-sgl-model-gateway.md:30
- --stream-interval 1: S/r-1-flags-and-defaults.md:25

## Troubleshooting (troubleshooting, 6 rows)
- Insufficient Memory, 0.872 automatic fraction: S/3-2-mem-fraction-static-and-startup-sizing.md:28
- ambiguous option --cuda-graph-max-bs: S/4-1-forwardmode-and-cuda-graphs.md:140
- Could not find nvcc: S/7-1-operating-sglang.md:20
- memory capacity is unbalanced: S/6-1-tp-size-dp-size-and-attn-dp-size.md:105
- KV cache pool is full, retract requests: S/2-3-admission-and-retraction.md:60
- #cached-token 0 on repeated prompts: S/3-4-prefix-friendly-prompts.md:9

## Glossary (glossary, 4)
- ITL: S/1-1-what-a-serving-engine-owns.md:31
- KV: S/3-1-kv-bytes-per-token-and-the-kv-pool.md:3
- Radix tree: S/3-3-radixcache.md:3
- MoE: S/6-2-moe-serving-deepep-and-eplb.md:3

## Questions (qa, 4)
- Queueing with free memory: S/2-3-admission-and-retraction.md:9
- lpm changes to FCFS above 128: S/2-2-the-scheduler-loop-and-schedule-policy.md:62
- Overlap scheduler default and MLX crash: S/2-4-the-overlap-scheduler.md:90
- Temperature 0 and batch size: S/4-6-deterministic-inference-and-logprobs.md:80

## Tips (tips, 4)
- Pin lmsysorg/sglang:v0.5.22, never latest: S/7-1-operating-sglang.md:7
- Start every server with --enable-metrics: S/5-2-the-metrics-endpoint.md:9
- Read max_total_num_tokens at startup: S/2-1-sglang-serve-and-the-three-processes.md:55
- Pass --random-range-ratio 1.0: S/5-1-sglang-benchmark-serving.md:85
