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
- Lesson-end Git workflow: 每学完一节课，集中保存学习记录后检查并提交本课相关变更，无需再次确认；仅暂存本课记录、练习产物及必要配置，排除虚拟环境、密钥和无关改动，遵循仓库提交与验证规则。默认仅本地提交，推送需用户明确要求。
- Restart: 用户明确选择重新开始全量学习；本轮不继承旧分级成绩、旧完成记录或旧断点。
- Next lesson: phases/00-setup-and-tooling/07-docker-for-ai
- Current checkpoint: 2026-10-04，00/06 Python Environments 已完成；课后答案 C、B、A，3/3（100%，独立作答；第3题将原文的最可能原因改为合理的可能原因，避免未经排查断定）。00/05 暖身 A、C 均正确，隐藏依赖复查通过。学习者手动在 WSL 验证仓库 .venv 的解释器、sys.prefix、sys.base_prefix 和 NumPy 路径；纠正了未激活时显式调用环境 Python 会使用系统包的误解，并通过 cd ~ 后相对路径指向主目录环境的实际输出区分相对路径与绝对路径。创建 learning-artifacts/00-06-python-environments/.venv-numpy1，安装 NumPy 1.26.4，实测仓库环境仍为 2.5.3；编写 pyproject.toml（NumPy 基础依赖、torch/llm 可选依赖），用 uv pip compile 生成 requirements.lock（numpy==2.5.3），再创建 .venv-locked 按锁文件安装并确认版本和路径。理解依赖范围、间接依赖、声明与锁文件、Git 中保留配置而排除环境、虚拟环境不隔离显卡驱动。教材 env_setup.sh 因工作副本 CRLF 在第二行失败；学习者仅转换该脚本为 LF 后完整运行，All checks passed，仓库 Python 3.12.14、NumPy 2.5.3、matplotlib 3.11.2、scikit-learn 1.9.1、pandas 3.0.6、jupyter_core 5.9.1，3x3 矩阵乘法通过，PyTorch 2.6.0+cu124 / CUDA True；新增 scikit-learn 及相关共6包。硬链接警告自动回退复制，安装成功。已解释脚本直接安装未固定版本的包名，不读取锁文件，检查通过不证明跨机器版本一致。未故意安装或卸载系统包，用独立环境实践替代教材全局安装练习；未安装 conda，未实际安装可选依赖或生成 uv.lock。下次进入 00/07 Docker for AI，先做00/06两道回忆，优先复查解释器选择。Phase 0 仍为 Do。
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
| 2026-10-04 | 00/05 | 3/3 (100%, 第2题讲解后确认) | 完成 WSL JupyterLab Notebook、计时、CSV与绘图、重启从头运行及教材脚本；澄清行列标签和隐藏状态，处理 Agg 警告。 |
| 2026-10-04 | 00/06 | 3/3 (100%) | 完成两环境 NumPy 版本隔离、项目依赖声明、锁文件生成与新环境重建；纠正解释器选择和相对路径误解，修正教材脚本 CRLF 后检查全通过。 |

## Review queue

- 暂无。00/05 的隐藏依赖已在 2026-10-04 暖身中复查通过。
