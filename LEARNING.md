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
- Next lesson: phases/00-setup-and-tooling/09-data-management
- Current checkpoint: 2026-10-10，00/08 Editor Setup 完成，课后 D、D、D，3/3（100%，独立作答；第3题已纠正教材对张量形状检查的过度表述）。Docker 暖身 2/2。已验证 VS Code 1.139.1 的 WSL 连接、仓库 .venv/bin/python、NumPy 2.5.3；Notebook 内核相同，保存输出含 array([0, 1, 2, 3, 4])。理解类型提示不强制运行时检查：double("3") 得到字符串 "33"，double(3) 得到 6。Pylance basic 已启用；扫描多个虚拟环境且停止超时后，显式启用 useDefaultExcludes 并重载窗口，类型诊断恢复；具体根因未通过单变量实验确定。Black 保存时格式化、Ruff F401 删除未用导入和 I001 导入分组已由学习者验证。启用 Notebook 输出滚动、88/120 列参考线；自动保存未验证。Remote SSH 打开 /data0/liujie，终端和编辑器运行均确认主机 iipl-100、解释器 /data0/liujie/miniconda3/bin/python；仅用于验证，没有安装远程依赖或执行训练。服务器 GPU0 可查询，GPU1 为 Prohibited，GPU2 设备句柄异常，未验证 CUDA 运算、未修改驱动或计算模式。远程练习文件留在服务器，本地不冒充该文件实测。工作区 .vscode/ 被仓库忽略，本课配置快照保存于 learning-artifacts/00-08-editor-setup/settings.json；练习脚本收尾移除磁盘中残留的 math。下次进入 00/09 Data Management，先做 Editor Setup 两题回忆，注意分辨静态诊断、运行时行为和解释器/内核。Phase 0 仍为 Do。
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
| 2026-10-08 | 00/07 | 3/3 (100%) | 完成 GPU 镜像构建、CUDA 点积、bind mount 持久化、Compose 服务名通信与 HTTP 端口映射；纠正 CMD 与持久化误解，复习 runtime/devel；未实际重建 runtime 对比大小或新增依赖。 |
| 2026-10-10 | 00/08 | 3/3 (100%) | 验证 WSL Python 与 Notebook、Pylance 类型检查、Black 格式化、Ruff 修复及 Remote SSH；纠正类型提示运行时强制检查的误解，恢复默认排除后诊断恢复；远程 GPU 异常未作修复。 |

## Review queue

- 暂无。00/05 的隐藏依赖已在 2026-10-04 暖身中复查通过。
