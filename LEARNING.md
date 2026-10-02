# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission

补齐 AI 工程全链路、加强研究基础、做出可用产品，并理解日常使用的 AI 系统。首个作品目标是 AI Agent。

从头完整学习本仓库的 20 个阶段、523 节课程，不跳过任何阶段。按仓库的 AGENTS.md 和原生学习技能执行，用中文分节讲解、逐步理解与实践。

## Placement

- Date: 2026-10-01
- Score: self-selected
- Entry point: Phase 0: Setup & Tooling
- Pace: ~10 hours/week
- Execution environment: 用户约定相关课程代码统一在本地 WSL2（Ubuntu-24.04）中运行；使用 Linux shell、路径和 WSL 内的解释器及依赖。当前课程环境是学习者在仓库内重新创建的 .venv；前序 Windows .venv 与 .venv-wsl 已由学习者清理，主目录的既有环境未搬迁或复制。
- Verified WSL environment: /mnt/d/JeremyLiew/Documents/ResHub/10-Projects/Code-Workspace/ai-engineering-from-scratch/.venv，Python 3.12.14；sys.executable 指向该环境的 bin/python，sys.prefix 指向该 .venv，sys.base_prefix 为 /home/jeremyliew7/.local/share/uv/python/cpython-3.12.14-linux-x86_64-gnu。仓库环境已通过课程 beginner --show-later 检查，Python/Git 2/2 必需项与 9 项后续工具均通过。NumPy 2.5.3；Node.js 22.23.3、pnpm 12.8.1 由 WSL 交互式 Bash 的 fnm 初始化；Rust/Cargo 1.98.1、Julia 1.13.1。PyTorch 2.6.0+cu124 实测 CUDA 可用，RTX 4060 Laptop GPU 张量位于 cuda:0，点积结果 14.0。
- Learning preferences: 中文分节讲解；环境操作由学习者按引导在 WSL 手动执行，助手可读取本聊天右侧终端核验输出。课后测验一次展示全部题目，学习者集中回答，再逐题反馈。
- Restart: 用户明确选择重新开始全量学习；本轮不继承旧分级成绩、旧完成记录或旧断点。
- Next lesson: phases/00-setup-and-tooling/04-apis-and-keys
- Current checkpoint: 2026-10-02，00/03 GPU Setup & Cloud 已完成，课后测验 B、B、C，3/3（100%）。学习者在仓库 WSL .venv 手动执行 nvidia-smi、PyTorch 检查及课程 gpu_check.py；PyTorch 2.6.0+cu124、CUDA 12.4 可用，RTX 4060 Laptop GPU 总显存 8.0 GiB（约 8.6 GB）。nvidia-smi 检查时显示 4492/8188 MiB 已用，不能把总显存当成全部可用显存。4000×4000 矩阵乘法原单次 CPU 0.276s、GPU 0.271s；补充实验先预热 3 次，再计时 10 次取平均，CPU 0.263008s、GPU 0.021619s，约 12.2 倍，GPU 计时不包含输入传输，结果仅适用于本次条件。学习者理解异步同步与预热、fp16 每参数 2 字节和 1B 权重约 2 GB；澄清参数容量只算权重、训练还需梯度/优化器状态/中间张量，batch 增大主要增加输入与中间张量。已讲解 Colab 的 GPU 入口、远程环境隔离及资源限制；按用户约定实验只在本地 WSL 完成，未启用 Colab 或租用云 GPU。Git 分支及远程配置沿用 00/02，本次没有暂存、提交或推送；课末记录尚未提交或推送。下次用原生 learn 进入 00/04 APIs & Keys，先做 00/03 两道回忆。Phase 0 仍为 Do。
- Source snapshot: 1bafaa88bb4668356791150bec3a6d7df38387eb
- Estimates: 下表采用 ROADMAP.md 各阶段标题的工时，合计 1,128 小时；与其开头及结尾总数不一致，仅作粗略参考，不承诺完课日期。

## Path

| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | 14 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 21 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP — Foundations to Advanced | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 43 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 32 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

## Progress log

| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-10-02 | 00/01 | 3/3 (100%) | 在仓库内手动搭建 WSL .venv，完成 CUDA 点积、环境检查与四语言 Hello World；理解硬链接与依赖隔离，修正了 Python 命令的嵌套引号。 |
| 2026-10-02 | 00/02 | 3/3 (100%) | 手动完成暂存提交、分支切换与合并、模型忽略规则、历史查看及 Fork 推送；纠正 --cache 拼写，区分提交署名与 HTTPS Token 认证。 |
| 2026-10-02 | 00/03 | 3/3 (100%) | 手动验证 WSL GPU 与 8 GiB 显存；预热 3 次、计时 10 次平均的矩阵乘法实测约 12.2 倍；澄清预热、中间张量和 fp16 仅算权重的容量限制。 |

## Review queue

暂无。00/01、00/02 与 00/03 课后测验均为 3/3（100%），无需加入复习队列。
