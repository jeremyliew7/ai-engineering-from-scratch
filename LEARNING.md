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
- Next lesson: phases/00-setup-and-tooling/05-jupyter-notebooks
- Current checkpoint: 2026-10-03，00/04 APIs & Keys 已完成，课后测验 A、D、B，3/3（100%）；00/03 两道回忆 B、C 均正确。学习者理解环境变量对子进程的继承、.env 不自动加载、字典 → JSON 文本 → UTF-8 字节的序列化与编码、json.loads 反序列化及数字与字符串的区别、SDK 对象属性与字典键读取的区别。在当前 WSL Bash 从 Windows 用户级或系统级环境变量导入 MIMO_API_KEY（未显示或保存密钥值），Python 检测为已设置，密钥前缀判定为按量付费 API；导入仅对当前 shell 及后续子进程有效。学习者手动安装 anthropic 1.11.0，硬链接失败后复制安装成功；使用 MiMo Anthropic 兼容接口、mimo-v2.6-pro、关闭思考、max_tokens=128 完成 SDK 调用（输入 17、输出 32 token，end_turn）和原始 HTTP 调用（HTTP 200，dict，输入 17、输出 28 token，end_turn）。使用独立假密钥验证 HTTP 401 / Invalid API Key / invalid_key，未修改真实环境变量；理解 429 限流需要等待与降低频率。已查看教材排错产物，指出不能打印密钥前缀，采用仅检查存在性的方式；教材注册赠送 5 美元不能视为保证。实践在 WSL 终端完成，未将课堂命令另存为源码文件；本课学习记录按用户要求提交到 codex/local-learning，未推送。下次用原生 learn 进入 00/05 Jupyter Notebooks，先做 00/04 两道回忆。Phase 0 仍为 Do。
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
| 2026-10-03 | 00/04 | 3/3 (100%) | 在 WSL 手动完成 MiMo SDK 与原始 HTTP 调用及假密钥 401 实验；深入理解序列化、UTF-8 编码、反序列化和 Python 类型，区分密钥保存位置与请求头位置。 |

## Review queue

暂无。00/01、00/02、00/03 与 00/04 课后测验均为 3/3（100%），无需加入复习队列。
