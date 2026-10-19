---
id: sglang-serving
title: LLM Serving with SGLang
code: LS
subtitle: Start, size, measure and fix an SGLang server. SGLang 0.5.22.
hue: 200
sources: manuals/sglang-101
source_hash: 2ab89184782f4c99
---

## Three processes
type: architecture
from: manuals/sglang-101/sections/1-2-one-request-end-to-end.md, manuals/sglang-101/sections/2-1-sglang-serve-and-the-three-processes.md, manuals/sglang-101/sections/2-2-the-scheduler-loop-and-schedule-policy.md

```arch
node | client | 1,1 | Client | POST /generate | client
node | tok | 2,1 | TokenizerManager | text to ids | process
node | sched | 3,1 | Scheduler | batches and KV pool | process
node | model | 3,2 | Model forward | prefill and decode | model
node | detok | 2,2 | Detokenizer | ids to text | process
edge | client | tok | HTTP
edge | tok | sched | ZMQ
edge | sched | model | run batch
edge | sched | detok | token ids
edge | detok | client | text
```

## One request
type: flow
from: manuals/sglang-101/sections/1-2-one-request-end-to-end.md

1. **Client**: `POST /generate` sends a five-token prompt.
2. **Scheduler**: `cached_tokens` is 2, so it computes 3 new tokens.
3. **Model**: prefill and decode return 12 tokens.
4. **Response**: `finish_reason` says `length`.
5. **Timing**: the request takes 950 ms end to end.

## Start a server
type: annotated-code
lang: bash
from: manuals/sglang-101/sections/2-1-sglang-serve-and-the-three-processes.md, manuals/sglang-101/sections/5-1-sglang-benchmark-serving.md, manuals/sglang-101/capture/README.md

```bash
SGLANG_USE_MLX=1 sglang serve --model-path mlx-community/Qwen3-0.6B-4bit --disable-cuda-graph --host 127.0.0.1 --port 30000 --enable-cache-report --enable-metrics --mem-fraction-static 0.4   # Apple silicon, MLX backend
sglang serve --model-path Qwen/Qwen3-30B-A3B-Instruct-2507 --host 127.0.0.1 --port 30000 --enable-cache-report --enable-metrics --mem-fraction-static 0.7   # NVIDIA GPU
python3 capture/run.py --check   # re-record and compare the stable facts
```

## Commands
type: command-table
from: manuals/sglang-101/sections/2-1-sglang-serve-and-the-three-processes.md, manuals/sglang-101/sections/3-2-mem-fraction-static-and-startup-sizing.md, manuals/sglang-101/sections/3-4-prefix-friendly-prompts.md, manuals/sglang-101/sections/5-2-the-metrics-endpoint.md, manuals/sglang-101/sections/2-2-the-scheduler-loop-and-schedule-policy.md, manuals/sglang-101/sections/4-3-quantization.md, manuals/sglang-101/sections/4-6-deterministic-inference-and-logprobs.md, manuals/sglang-101/capture/README.md

| Command | What it does |
|---|---|
| `sglang serve --model-path <model> --port <port>` | Starts the server. It is the recommended entry point. |
| `--enable-cache-report` | Adds `cached_tokens` to OpenAI replies. |
| `--enable-metrics` | Serves `/metrics`. Off by default. |
| `--mem-fraction-static <fraction>` | Caps the KV pool on a shared machine. |
| `--schedule-policy lpm` | Orders the queue by cached prefix. Default is fcfs. |
| `--kv-cache-dtype fp8_e4m3` | Halves bytes per token. Check accuracy first. |
| `--enable-deterministic-inference` | Fixes reduction order for tested backends. |
| `python3 capture/run.py --check` | Re-records the kit and compares stable facts. |

## Four numbers
type: concepts
from: manuals/sglang-101/sections/1-1-what-a-serving-engine-owns.md, manuals/sglang-101/sections/3-1-kv-bytes-per-token-and-the-kv-pool.md

- **TTFT**: time to first token. Prefill and queueing set it.
- **TPOT**: average gap between tokens after the first. Decode sets it.
- **Throughput**: output tokens per second across users. Batching sets it.
- **Goodput**: requests per second that meet a TTFT and a TPOT target.
- **KV pool**: fixed slots for every running token, sized by `max_total_num_tokens`.

## Order of changes
type: flow
from: manuals/sglang-101/sections/7-1-operating-sglang.md, manuals/sglang-101/sections/4-2-attention-backend.md, manuals/sglang-101/sections/6-1-tp-size-dp-size-and-attn-dp-size.md

1. **Measure**: run `sglang.benchmark.serving` at three concurrency levels.
2. **Memory**: set `--mem-fraction-static` on a shared machine.
3. **Prompts**: put shared text first in every prompt.
4. **Concurrency**: cap `--max-running-requests` at the measured knee.
5. **Kernels and scale**: change one flag per run. Add `--tp-size` only when weights do not fit.

## Defaults
type: defaults
from: manuals/sglang-101/sections/r-1-flags-and-defaults.md, manuals/sglang-101/sections/2-2-the-scheduler-loop-and-schedule-policy.md, manuals/sglang-101/sections/6-3-prefill-decode-disaggregation.md, manuals/sglang-101/sections/6-4-sgl-model-gateway.md

| Setting | Default | Note |
|---|---|---|
| `--tp-size` | 1 | One GPU per copy. Raise only when weights do not fit. |
| `--schedule-policy` | fcfs | Try lpm only after you measure hits. |
| `--radix-eviction-policy` | lru | Keep until a hit rate shows a reason. |
| `--schedule-conservativeness` | 1.0 | Raise when the log shows retractions. |
| `--decode-log-interval` | 40 | Decode lines in the scheduler log. |
| `--num-reserved-decode-tokens` | 512 | Decode tokens reserved when a request joins. |
| `--cache-threshold` | 0.3 | Gateway match rate for prefix affinity. |
| `--stream-interval` | 1 | Streams after every step. |

## Troubleshooting
type: troubleshooting
from: manuals/sglang-101/sections/3-2-mem-fraction-static-and-startup-sizing.md, manuals/sglang-101/sections/4-1-forwardmode-and-cuda-graphs.md, manuals/sglang-101/sections/7-1-operating-sglang.md, manuals/sglang-101/sections/6-1-tp-size-dp-size-and-attn-dp-size.md, manuals/sglang-101/sections/2-3-admission-and-retraction.md, manuals/sglang-101/sections/3-4-prefix-friendly-prompts.md

| Symptom | Cause | Fix |
|---|---|---|
| `Insufficient Memory` on a shared Mac | Automatic fraction was 0.872 | Pass `--mem-fraction-static 0.4` |
| `ambiguous option: --cuda-graph-max-bs` | Flag split in v0.5.22 | Use `--cuda-graph-max-bs-decode` |
| `Could not find nvcc` | No CUDA toolkit at `cuda_home` | Set `CUDA_HOME` to a toolkit |
| `The memory capacity is unbalanced` | Another process uses one TP GPU | Use `--dp-size` or free the memory |
| `KV cache pool is full. Retract requests.` | Admission forecast too bold | Raise `--schedule-conservativeness` to 1.3 |
| `#cached-token: 0` on repeated prompts | A changing id near the start | Move the id to the end |

## Glossary
type: glossary
from: manuals/sglang-101/sections/1-1-what-a-serving-engine-owns.md, manuals/sglang-101/sections/3-1-kv-bytes-per-token-and-the-kv-pool.md, manuals/sglang-101/sections/3-3-radixcache.md, manuals/sglang-101/sections/6-2-moe-serving-deepep-and-eplb.md

- **ITL**: inter-token latency. The gap between two output tokens.
- **KV**: stored keys and values, one pair per token per layer.
- **Radix tree**: index of cached token runs for prefix reuse.
- **MoE**: mixture of experts. Few experts run for each token.

## Questions
type: qa
from: manuals/sglang-101/sections/2-3-admission-and-retraction.md, manuals/sglang-101/sections/2-2-the-scheduler-loop-and-schedule-policy.md, manuals/sglang-101/sections/2-4-the-overlap-scheduler.md, manuals/sglang-101/sections/4-6-deterministic-inference-and-logprobs.md

- **Why do requests queue with free memory?** Admission forecasts future tokens. Queueing protects running requests.
- **Why does lpm not help?** Above 128 waiting requests it changes to FCFS.
- **Is the overlap scheduler safe to keep?** It is the default. Do not add `--disable-overlap-schedule` on MLX at v0.5.22.
- **Is temperature 0 enough for the same output?** No. Batch size changes results. Use `--enable-deterministic-inference` and test.

## Tips
type: tips
from: manuals/sglang-101/sections/7-1-operating-sglang.md, manuals/sglang-101/sections/5-2-the-metrics-endpoint.md, manuals/sglang-101/sections/2-1-sglang-serve-and-the-three-processes.md, manuals/sglang-101/sections/5-1-sglang-benchmark-serving.md

- Pin `lmsysorg/sglang:v0.5.22`. Never deploy `latest`.
- Start every server with `--enable-metrics`.
- Read `max_total_num_tokens` in the startup log after every change.
- Pass `--random-range-ratio 1.0` in every benchmark.
