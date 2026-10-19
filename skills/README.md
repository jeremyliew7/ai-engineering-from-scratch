# 本项目 Skills 使用指南

本目录保存 AI Engineering from Scratch 的技能源码，涵盖互动学习、项目实践、认证准备、图解与手册制作，以及课程仓库维护。Skill 是供 AI 助手按需读取的工作流程，可以附带参考资料、模板和脚本；注册技能本身不会启动课程、运行脚本或完成练习。

本文根据 2026-10-19 的本地配置整理：本项目已注册 **17 个技能**。具体执行规则以各技能的 `SKILL.md` 为准，本地学习流程同时遵循 [AGENTS.md](../AGENTS.md) 和 [AGENTS.override.md](../AGENTS.override.md)。

## 从哪里开始

| 你的需求 | 优先使用 |
|---|---|
| 同步上游、维护关联本地产物并说明变更 | `course-update` |
| 从当前断点继续通用课程 | `learn` |
| 第一次制定通用课程学习计划 | `start-learning` |
| 不确定自己的基础适合从哪里开始 | `find-your-level` |
| 想找某个知识点对应的课程 | `course-guide` |
| 检查一个阶段是否掌握 | `check-understanding` |
| 分阶段动手做一个项目 | `build-project` |
| 集中学习 MCP、Agent Skills 或逆向工程 | 对应的 `learn-*` 技能 |
| 生成静态机制图 | `blueprint-figure` |
| 用动画或滑块解释变量怎样影响结果 | `motion-figure` |
| 将整个流程做成可操作的机器演示 | `isometric-explainer` |
| 编写可追溯、可复核的长篇技术手册 | `write-manual` |

已有学习进度时，直接使用对应的继续学习技能。无需为了继续一课而重新运行入门评估或创建第二份学习计划。

## 1. 入门与通用课程：5 个技能

| 技能 | 用途 | 示例请求 |
|---|---|---|
| [start-learning](start-learning/SKILL.md) | 访谈学习目标、评估起点，建立或调整通用课程计划 | “使用 start-learning，为我制定课程学习计划。” |
| [find-your-level](find-your-level/SKILL.md) | 用诊断题定位知识基础，建议课程起点 | “使用 find-your-level，评估我适合从哪个阶段开始。” |
| [course-guide](course-guide/SKILL.md) | 根据问题、主题或故障，定位相关课程和下一步入口 | “使用 course-guide，找讲 KV cache 的课程。” |
| [learn](learn/SKILL.md) | 读取学习偏好和断点，分步讲解、练习、测验并维护课程进度 | “使用 learn，从 LEARNING.md 的 Current checkpoint 继续。” |
| [check-understanding](check-understanding/SKILL.md) | 根据指定阶段的教材生成 8 道诊断题，反馈薄弱点和复习课程 | “使用 check-understanding，检查我对 Phase 00 的掌握。” |

`find-your-level` 用于判断起点，`check-understanding` 用于检验某一阶段，`learn` 则负责持续学习。`course-guide` 主要负责找路，不替代一整课的互动教学。

## 2. 项目、专题与认证：6 个技能

| 技能 | 用途 | 进度文件 |
|---|---|---|
| [build-project](build-project/SKILL.md) | 按项目阶段推进：阅读任务、预测、自己编写代码、运行评分器、复盘。提供提示，不直接交付完整解答 | `PROJECTS-LEARNING.md` |
| [learn-mcp](learn-mcp/SKILL.md) | 专题学习 MCP 客户端、服务器、传输、安全、网关及验证；保留实际请求与响应证据 | `MCP-LEARNING.md` |
| [learn-agent-skills](learn-agent-skills/SKILL.md) | 学习技能发现、调用、安全、评估、打包和移植；要求真实宿主上的操作证据 | `AGENT-SKILLS-LEARNING.md` |
| [learn-reverse-engineering](learn-reverse-engineering/SKILL.md) | 学习二进制格式、反汇编、控制流、伪代码、类型恢复与验证；仅分析自己编译或获书面授权的程序 | `REVERSE-ENGINEERING-LEARNING.md` |
| [claude-certification](claude-certification/SKILL.md) | 选择 Claude 认证准备路线，进行互动教学、实验、诊断、模拟考试和薄弱项复习 | `CLAUDE-CERTIFICATION.md` |
| [mcpa-certification](mcpa-certification/SKILL.md) | 按仓库的 MCPA 路线学习，执行协议实验、产物验证、诊断和模拟考试 | `MCPA-CERTIFICATION.md` |

示例请求：

```text
使用 build-project，先列出当前已就绪的项目，让我选择。
使用 learn-mcp，继续 MCP 专题路线。
使用 learn-agent-skills，从技能发现与调用开始学习。
使用 learn-reverse-engineering，检查前置条件后开始第一课。
使用 claude-certification，先比较仓库提供的准备路线。
使用 mcpa-certification，先做诊断，再制定学习计划。
```

专题顺序由 [learning-paths/](../learning-paths/) 中对应的清单决定，不一定等于课程编号顺序。各路线独立保存进度，不应混入通用课程的 `LEARNING.md`。MCP 路线兼容旧进度文件名 `MCP-ENGINEERING-LEARNING.md`，迁移由 `learn-mcp` 处理。

认证技能提供的是仓库维护的独立学习与练习流程，不负责报名或颁发证书，也不保证通过考试。考试信息以对应 `certifications/` 目录的来源记录及当前官方规则为准。

## 3. 图解与手册制作：5 个技能

这些技能用于制作内容，不会替代学习路线，也不会自动修改学习进度。

| 技能 | 适用场景与产物 | 使用成本和边界 |
|---|---|---|
| [blueprint-figure](blueprint-figure/SKILL.md) | 静态 SVG 机制图：时序、结构、数据流、对比、时间线、树、状态机、决策和分层，共九类 | 从真实代码、规范或日志取名；附生成脚本，检查字号、重叠、配色和可访问性。数值趋势图应另用绘图工具 |
| [motion-figure](motion-figure/SKILL.md) | SVG 动画、滑块实验、交互式机制页面及抖动纹理页眉 | 课内图使用课程图形运行时；独立机制页有 HTML 模板。需要验证交互、窄屏和减少动态效果的行为 |
| [isometric-explainer](isometric-explainer/SKILL.md) | 把流程表现为有工位、有运动部件的等距机器，支持运行、单步、故障与修复 | 先建立可测试的确定性状态模型，再绘制几何结构。需要模型测试和浏览器截图验证，成本高于普通图解 |
| [course-style](course-style/SKILL.md) | 本课程的配色、字体、图号、布局、英文写作及无障碍参考 | 主要是规范库，没有独立绘图流程；规则针对本课程风格，不应默认套用于其他品牌或中文写作 |
| [write-manual](write-manual/SKILL.md) | 为固定版本的协议、工具或运行时编写系统手册，包含来源、采集记录、图解和审计 | 面向约 60—100 页的长篇文档，需要可复核的采集证据；普通短笔记不必采用整套结构 |

示例请求：

```text
使用 blueprint-figure，根据这段真实代码画一张训练步骤时序图。
使用 motion-figure，做一个能调整学习率的交互演示，并说明模型的简化条件。
使用 isometric-explainer，把有缓存、重试和失败分支的请求流程做成机器演示。
使用 course-style，检查这张课程图的配色、字体和可访问性。
使用 write-manual，先为指定版本的工具拟定来源清单、采集方案和目录。
```

`blueprint-figure` 和 `motion-figure` 自带必要的参考资料，可独立使用。需要严格统一课程风格时，再配合 `course-style`。`write-manual` 会使用静态图规范；`isometric-explainer` 自带几何工具和模板。

这些包包含本地脚本和模板，但不等于运行依赖已经安装。绘图构建通常需要 Node.js，交互页面还需要浏览器验证；课程实验、认证和手册采集所需的 Python、编译器或服务，按具体任务检查。确定性模拟的时间与数字应标明为模拟值，不能当作真实系统的实测结果。

## 4. 课程仓库维护：1 个技能

| 技能 | 用途 | 示例请求 |
|---|---|---|
| [course-update](course-update/SKILL.md) | 同步远程，追踪更新对已有译文、练习、笔记、配置和文档的影响，修改关联内容并逐项说明；维护技能清单、按选择注册技能，验证并本地提交 | “使用 course-update，更新课程仓库并同步受影响的本地产物，告诉我修改了哪些内容。” |

该技能把本次完整维护流程封装为一个入口。关联更新不限于译文：例如源函数改名要检查练习导入，课程配置路径变化要检查笔记和配置，技能新增要检查目录入口及 README。需要重跑才能证明的实验结果会标为待验证，不会直接改写成绩或完成记录。

默认执行完整维护并提交本轮相关变更；可以限定“只检查”“维护已合入更新，不再拉取”“暂不提交”。新增技能仍先列清单供选择，已有明确授权则直接执行；推送仍需明确授权。

## 在 Codex 中怎样调用

最直接的方式是在聊天中明确写出技能名和目标：

```text
请使用 learn，读取我的学习偏好和断点，继续通用课程。
请使用 blueprint-figure，画出本段代码的数据流，并注明依据。
```

Codex CLI 和 IDE 扩展也支持通过 `/skills` 选择，或用 `$技能名` 显式提及。桌面界面的选择入口以实际版本为准；直接写“使用 skill-name”不依赖选择器的位置。自然语言请求与技能描述匹配时，助手也可以自动选用技能。

`/learn` 这类独立斜杠命令是部分宿主的约定，不应当作所有客户端通用的调用语法。技能名称可跨宿主复用，调用入口由宿主决定。[Codex 官方技能说明](https://learn.chatgpt.com/docs/build-skills)

## 本项目的目录与注册方式

| 位置 | 作用 |
|---|---|
| `skills/<name>/SKILL.md` | 技能源码：用途、触发条件和执行流程 |
| `skills/<name>/references/` | 需要时读取的规范和参考资料，部分技能提供 |
| `skills/<name>/templates/`、`kit/` | 模板或工具库，部分技能提供 |
| `.agents/skills/<name>/` | 本地 Codex 的项目级发现入口；当前为指向对应源码目录的 Windows Junction |
| `.claude/skills/` | 仓库面向 Claude Code 的发现位置，不是本地 Codex 的注册入口 |

本机的 17 个入口都指向本仓库的 `skills/`，不是另外复制的一套源码。修改或同步源码后，入口会读取对应文件；若新增一个技能目录，仍需为它建立发现入口。

2026-10-19 已通过 Codex app-server 的 `skills/list` 复核本次新增的六个技能：`blueprint-figure`、`motion-figure`、`isometric-explainer`、`course-style`、`write-manual`、`learn-reverse-engineering`，均为 `scope=repo`、`enabled=true`。项目级注册让它们能在本仓库中发现；需要其他项目使用时，另行选择注册范围。

Windows Junction 是本机文件系统入口。本仓库源码同步到新机器、目录移动或在 WSL 中运行另一份 Codex 客户端后，应重新检查发现结果，不能仅凭本机曾成功注册就认定可用。

## 本地学习约定

- 通用学习从 `LEARNING.md` 的学习偏好与 Current checkpoint 继续；专题和项目读取各自的进度文件。
- 新课先核对完整英文源文，保存完整中文译文并在聊天中完整交付，再进入分步互动教学。译文放在 [learning-artifacts/course-translations/](../learning-artifacts/course-translations/)。
- 普通答题直接反馈，文件更新集中在课末或暂停时；明确要求保存时按当次要求执行。
- 学习环境沿用当前约定的 WSL 环境；安装、迁移或删除环境按用户授权执行。
- 学习者实践使用独立产物目录或工作区，不覆盖课程参考代码。项目导师提供提示，不把参考解答当作学习者作业。
- 每课结束后，按本地约定验证并提交本课相关变更；推送需要明确授权。

本指南不保存课程成绩或断点，避免与各路线的进度文件形成两份记录。

## 更新和排查

在仓库根目录的 PowerShell 中查看入口：

```powershell
Get-ChildItem -LiteralPath .agents/skills -Directory |
    Select-Object Name, LinkType, Target

Test-Path -LiteralPath .agents/skills/blueprint-figure/SKILL.md
```

更新后检查以下事项：

1. 对应 `skills/<name>/SKILL.md` 存在，参考文件和模板齐全。
2. `.agents/skills/<name>` 指向当前仓库中的正确目录。
3. 客户端技能清单能发现它，且没有被禁用；目录存在不等于已验证客户端加载。
4. 先直接点名技能尝试调用。Codex 通常自动检测变化；仍未显示时可重启客户端。
5. 保持一份源码和对应入口，避免复制旧版后出现同名技能。维护本清单时同步增删条目。

部分上游技能介绍仍保留旧的课程总数。选择课程以当前 [README.md](../README.md)、[ROADMAP.md](../ROADMAP.md) 和路线清单为准，不根据技能描述里的历史数字推断当前课程规模。
