# 00/09 数据管理学习记录

- 日期：2026-10-10
- Editor Setup 暖身：A、D，2/2，不计本课成绩。
- 课后测验：C、C、A，3/3（100%，独立作答）。
- 环境：WSL Ubuntu-24.04，仓库 `.venv/bin/python`；安装日志确认 datasets 5.1.0、huggingface-hub 2.2.0、pyarrow 26.0.0。
- 以下实践结果来自读取学习者本聊天终端；镜像配置验证由助手执行，二者分开记录。

## 学习者实测

1. IMDB 普通加载：train 25,000、test 25,000、unsupervised 50,000 条；记录包含 text、label。理解字符串键需要引号，第二条记录用索引 1。
2. 流式读取：类型为 IterableDataset；提前停止时打印 0、1、2，移除停止条件后最后索引为 24999。
3. IMDB 固定 seed=42 打乱后取 1,000 条：CSV 1,321,259 字节、Parquet 852,732 字节，后者约小 35.5%。只比较大小，未做读取速度基准。
4. 两次划分得到 700/150/150；第二次 test_size=150/850。验证集前五个 row_id 为 869、584、589、667、95。
5. 重复划分完全一致、三个集合 ID 两两无交集、并集覆盖全部 1,000 条，三项均 True。row_id 是抽样后的位置编号，不是原始 IMDB ID；未检查文本重复或分组泄漏。
6. all-MiniLM-L6-v2 的 config.json 为 612 字节；local_files_only=True 读取缓存成功。仅下载配置，未下载模型权重或执行模型推理。
7. 教材 code/data_utils.py 运行至结束：Rotten Tomatoes 训练集 8,530 条，流式读取 3 条；500 条导出 CSV/JSON/Parquet 为 59,539/68,473/41,350 字节；划分 400/50/50；Parquet 重载 500 条。前 100 条指纹 95b6a4c115c8ac8b；当次 datasets 缓存统计 29 个文件、129.9 MiB（脚本标为 MB）。脚本末尾成功提示是演示完成，不等于完整测试套件通过。

练习导出位于 WSL `/tmp/ai-data-management` 和 `/tmp/data_utils_demo`，不纳入 Git，也不视为永久保存。教材可复用工具仍为 `phases/00-setup-and-tooling/09-data-management/code/data_utils.py`。

## 需要下次回忆的概念

- 第二次划分以剩余数据为基数：先留出 15%，再取 150/850；先留出 20%，再取 150/800。首次选 0.15，解释后纠正。
- local_files_only=True 禁止联网，缓存缺失会报错；首次误认为自动下载，解释后完成成功缓存实测，尚未做缓存缺失实验。
- .gitignore 忽略未跟踪文件，不影响已有跟踪；git rm --cached 移除索引条目、保留磁盘文件，提交后当前版本不再跟踪，但旧提交仍保留文件。经过多轮澄清后确认“本地保留，旧提交保留”。未实际执行历史重写或移除权重。
- 小文件不等于可以安全提交；处理脚本和无敏感信息的版本/种子配置适合提交。DVC 用于需要数据版本追踪和跨机器复现的场景，未配置或运行 DVC/Git LFS。

## 教材边界与纠正

- 正文示例的两次划分实际为 70/10/20，不是前文举例的 80/10/10。
- 固定种子需配合相同数据、顺序和算法；流式读取内存取决于缓冲及处理，不能保证绝对恒定。
- Parquet 的体积和读取优势取决于数据、压缩和读取方式，不是所有 AI 数据的通用最佳格式。
- 数据指纹仅覆盖前 100 条；数据集划分和未见数据评估也不能单独保证完全避免过拟合。
- 未执行扩展练习 GLUE/MRPC、C4 10 秒流式计数或完整模型 snapshot 下载。

## 本次另行授权的镜像配置

以下为机器配置，未将虚拟环境、缓存、系统配置副本或密钥纳入仓库。

| 工具 | 配置后的源 | 验证范围 |
|---|---|---|
| uv | https://mirrors.ustc.edu.cn/pypi/simple | 用户配置被读取，依赖解析成功 |
| npm / pnpm | https://registry.npmmirror.com | 保留已有配置并检查 |
| APT | https://mirrors.ustc.edu.cn/ubuntu/ | 含 noble-security，签名校验保留；apt-get update 成功 |
| rustup | https://rsproxy.cn；更新 https://rsproxy.cn/rustup | 端点可访问，未升级工具链 |
| Cargo | sparse+https://mirrors.ustc.edu.cn/crates.io-index/ | 下载 serde 验证 |
| Julia 包管理 | https://mirrors.sjtug.sjtu.edu.cn/julia | 获取注册表成功，实测重定向至北大 |
| fnm / Node.js | https://mirrors.ustc.edu.cn/node | 获取版本列表成功 |
| Docker Hub | https://docker.m.daocloud.io | Desktop 重启后引擎列出镜像源；hello-world 拉取检查成功、显示已有最新镜像，不能证明新下载的层经过镜像 |
| Hugging Face | https://hf-mirror.com | 课程 SDK 查询 IMDB、下载 README 成功；后续学习者加载数据与模型配置成功 |

uv 配置为 `~/.config/uv/uv.toml`；环境变量集中在 `~/.config/download-mirrors.sh`，由 .bashrc/.profile 加载；Cargo 使用 `~/.cargo/config.toml`；Julia 还配置 `~/.julia/config/startup.jl`。APT 配置 `/etc/apt/sources.list.d/ubuntu.sources`；Docker Desktop 使用 Windows `C:\Users\JeremyLiew\.docker\daemon.json`。已有文件修改前备份至 `~/.config/mirror-backups/`、`/root/mirror-backups/` 或 daemon.json 同目录带时间戳的备份。

中科大 Julia 镜像文档明确停止服务；中科大 Rust 工具链探测 404，因此选用上述替代源。镜像可用性随时间变化，这些是本次验证结果。安装提示硬链接失败后复制，安装成功，未为此改动 link-mode。

## 下一课

00/10 Terminal & Shell；先回忆缓存缺失行为、划分基数或 Git 历史保留。本阶段仍未结束。
