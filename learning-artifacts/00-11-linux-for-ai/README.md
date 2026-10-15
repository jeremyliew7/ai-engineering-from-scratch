# 00/11 Linux for AI 学习记录

- 学习日期：2026-10-11 开始，2026-10-15 完成。
- 课程源：phases/00-setup-and-tooling/11-linux-for-ai/docs/en.md。
- 教材：../course-translations/00-11-linux-for-ai-zh.md；已在本聊天完整交付，源 SHA-256 与保存记录一致，19 个代码块内容一致。
- 暖身：Terminal & Shell 两题均正确；重定向顺序预测正确（仅口头预测，未实测）。
- 课后测验：C、C、D，3/3（100%，独立作答）。

## 已核验的实操

- WSL 主目录创建 linux-ai-practice，touch 创建 model.py、config.yaml、.env.example；ls -la 显示隐藏文件，ls -l 隐藏该文件。
- hello.sh 初始权限 -rw-r--r--，直接执行报 Permission denied；bash hello.sh 成功输出 Hello Linux；chmod u+x 后权限 -rwxr--r--，直接执行成功。
- 后台 sleep 300 的 PID 为 2382；ps 显示 S/sleep；kill 后只剩 ps 表头，Shell 报 Terminated。
- df 检查主目录与仓库：WSL 文件系统可用 944G，D 盘可用 967G（当时快照，WSL 实际增长还受宿主磁盘空间约束）。
- du 显示练习目录 8.0K、缓存 6.0G；缓存排名 uv 5.8G、huggingface 211M，其余各不足 5M。总计与子目录不能重复相加。
- 终端可见 apt 完成 curl 等更新并安装 python3-venv 及依赖；whoami 输出 jeremyliew7。未据此声称完整系统升级或 htop 实测完成。

## 理解与纠正

- 脚本缺少 x 限制直接执行；bash hello.sh 是 Bash 读取脚本，要求相应读取及路径访问权限。学习者起初不知道此区别，解释后正确说明缺少读取权限的结果。
- 数字权限 rwxr--r-- 对应 744；chmod 修改权限，chown 修改所有权。
- 主目录创建个人文件不需 sudo，root 所有的目录可能阻碍后续写入。
- apt update 刷新索引；upgrade 升级软件；install 也可更新指定包。
- start 立即启动，enable 设置开机启动；SIGTERM 与 SIGKILL 的清理机会不同。
- df 查目标文件系统剩余空间，du 查目录占用；pip 缓存清理不等于 uv 缓存清理。
- scp 前源后目标；rsync 源路径尾斜杠表示复制内容。
- 远程 tmux 通常可抵御客户端断网，无法保留服务器重启前的训练进程。
- CRLF 导致解释器路径异常时应转为 LF，而非增加执行权限。
- echo 时误拼 pracitice_pid 导致空输出；后续 practice_pid 正确，进程实验成功。

## 实践边界与下一课

- 本课未进行真实远程 scp/rsync、systemctl 服务变更、CRLF 转换或缓存清理；tmux/htop 沿用上一课经验，本课未重新实测。
- 练习文件保留在 WSL ~/linux-ai-practice，未复制环境或缓存进仓库。
- 下一课：00/12 Debugging & Profiling。先按 learn 进行两道本课回忆题，新课完整译文须先核对、保存并在聊天交付。
