---
type: lesson-translation
phase: "00"
lesson: "03"
translated: 2026-10-11
translation_method: direct-new-translation
updated: 2026-10-19
update_method: upstream-delta-translation
source_path: phases/00-setup-and-tooling/03-gpu-setup-and-cloud/docs/en.md
source_commit: 4b842f93e35f8f3e7f2b825a81ae9b08dc32194c
source_last_commit: e6014b07fd44bc36f2a8e21ca9f64ce9d9309cf9
source_sha256: 1e6fdb7c16aeab51fb498a3b0d5fe984dd1a67e082d618bf30d1081639502809
---

# GPU 配置与云计算

> 学习时使用 CPU 训练没有问题；进行实际的大规模训练，则需要 GPU。

**类型：** 动手构建
**语言：** Python
**前置要求：** Phase 0，第 01 课
**时间：** 约 45 分钟

## 学习目标

- 使用 `nvidia-smi` 和 PyTorch CUDA API 验证本地 GPU 是否可用。
- 为 Google Colab 配置 T4 GPU，开展免费的云端实验。
- 对比 CPU 与 GPU 的矩阵乘法耗时，计算加速比。
- 用 fp16 的经验规则，估算显存能够容纳的最大模型。

## 问题

Phase 1—3 的大多数课程都可以在 CPU 上运行。但开始训练 CNN、Transformer 或 LLM 时（Phase 4 及之后），就需要 GPU 加速。原文举例：CPU 上运行 8 小时的训练，GPU 上可能只需 10 分钟。

有三种选择：本地 GPU、云 GPU，或免费的 Google Colab。

## 核心概念

```
Your options:

1. Local NVIDIA GPU
   Cost: $0 (you already have it)
   Setup: Install CUDA + cuDNN
   Best for: Regular use, large datasets

2. Google Colab (free tier)
   Cost: $0
   Setup: None
   Best for: Quick experiments, no GPU at home

3. Cloud GPU (Lambda, RunPod, Vast.ai)
   Cost: $0.20-2.00/hr
   Setup: SSH + install
   Best for: Serious training, large models
```

图示对比 CPU 与 GPU 的并行计算结构，说明 GPU 为什么适合张量和矩阵计算。

```figure
s0-gpu-dispatch
```

此标记对应课程网站的 GPU 并行计算交互图。

## 动手构建

### 方案 1：本地 NVIDIA GPU

先检查是否有 GPU：

```bash
nvidia-smi
```

安装支持 CUDA 的 PyTorch：

```python
import torch

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
```

### 方案 2：Google Colab

1. 打开 [colab.research.google.com](https://colab.research.google.com)。
2. 选择 Runtime（运行时）> Change runtime type（更改运行时类型）> T4 GPU。
3. 运行 `!nvidia-smi` 验证。

可以把本课程的 Notebook 直接上传到 Colab。

### 方案 3：云 GPU

如果使用 Lambda Labs、RunPod 或 Vast.ai：

```bash
ssh user@your-gpu-instance

pip install torch torchvision torchaudio
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

这组命令用于连接远程机器，并在远程配置训练环境。

### 没有 GPU？没关系

大多数课程支持 CPU。需要 GPU 的课程会明确说明，并提供 Colab 链接。

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using: {device}")
```

代码根据 CUDA 是否可用来选择运算设备。

## 动手构建：GPU 与 CPU 性能对比

```python
import torch
import time

size = 5000

a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"CPU: {cpu_time:.3f}s")

if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")

    torch.cuda.synchronize()
    start = time.time()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    print(f"GPU: {gpu_time:.3f}s")
    print(f"Speedup: {cpu_time / gpu_time:.0f}x")
```

代码创建矩阵，分别在 CPU 与 GPU 上执行矩阵乘法，并计算耗时和加速比。应结合下面的校注理解测量边界。

## 练习

1. 运行上面的性能测试，对比 CPU 与 GPU 耗时。
2. 如果没有 GPU，就在 Google Colab 上运行并比较。
3. 查看 GPU 显存容量，估算能容纳的最大模型。经验规则：fp16 每个参数占 2 字节。

### 练习提示

**练习 1.** 原样运行“动手构建”部分的代码，记下 CPU 耗时、GPU 耗时和加速比所在行。再运行一次；第一次 GPU 运行包含启动开销，因此应比较第二次的数字。

**练习 2.** 在 Colab 中选择 Runtime > Change runtime type > GPU，然后将基准测试粘贴到一个单元格中。先在另一个单元格运行 `!nvidia-smi`；它必须显示 GPU 名称，基准测试结果才有意义。

**练习 3.** 像 `code/gpu_check.py` 那样，用 `torch.cuda.get_device_properties(0).total_memory / 1e9` 读取总显存。将以字节计的显存除以 2，得到 fp16 的参数数量，再留出余量，因为激活值和 CUDA 上下文也占显存。

## 关键术语

| 术语 | 常见说法 | 实际含义 |
|---|---|---|
| CUDA | “GPU 编程” | NVIDIA 的并行计算平台，使代码能在 GPU 上运行 |
| VRAM | “显存” | GPU 上的视频内存，与系统内存分开；容量会限制模型规模 |
| fp16 | “半精度” | 16 位浮点数，内存占用为 fp32 的一半；原文称精度损失较小 |
| Tensor Core | “快速矩阵硬件” | 为矩阵乘法设计的专用 GPU 核心；原文称比普通核心快 4—8 倍 |

## 译者校注

- 8 小时与 10 分钟、4—8 倍都是原文示例或概括，不能作为具体任务的速度承诺。
- GPU 运算通常异步执行。可靠计时需要预热、重复测量，并在计时边界同步；单次冷启动结果可能误导。
- 每参数 2 字节仅估算 fp16 权重。训练还需要梯度、优化器状态和中间激活，不能把该结果直接当作可训练模型规模。
- Colab 的免费 GPU 型号、额度和可用性取决于当时服务情况，原文选项不构成资源保证。
