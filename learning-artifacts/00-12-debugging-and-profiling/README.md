# 00/12 Debugging and Profiling 学习记录

- 学习日期：2026-10-15 开始，2026-10-19 完成。
- 学习会话：Day7 00/12 Debugging and Profiling；Day7 由学习者确认，跨自然日沿用。
- 课程源：[英文教材](../../phases/00-setup-and-tooling/12-debugging-and-profiling/docs/en.md)。
- 教材：[完整中文译文](../course-translations/00-12-debugging-and-profiling-zh.md)，已在本聊天完整交付；源版本、哈希及校注见译文与教材清单，22 个原文代码块保持一致。
- 课后测验：B、C、D，3/3（100%，独立作答；按课程原题评分）。
- 实操由学习者在 WSL Ubuntu-24.04 执行；证据来自本聊天终端核验、TensorBoard 页面核验，以及学习者提供的 VS Code 调试输出。
- 课末依赖元数据核验：torch 2.6.0+cu124、NumPy 2.5.3、TensorBoard 2.21.0、line_profiler 5.0.2、memory_profiler 0.61.0、psutil 7.2.2；解释器指向仓库 WSL .venv/bin/python。

## 保留的练习

| 文件 | 用途 |
|---|---|
| [breakpoint_practice.py](breakpoint_practice.py) | 在损失超阈值或为 NaN 时进入 pdb；运行时会等待交互。 |
| [logging_practice.py](logging_practice.py) | INFO、WARNING、ERROR 的终端与文件输出；ERROR 消息不自动终止程序。 |
| [timing_practice.py](timing_practice.py) | 比较模拟数据加载与前向计算的耗时。 |
| [profile_practice.py](profile_practice.py) | 用 cProfile 区分函数自身耗时与累计耗时。 |
| [line_profile_practice.py](line_profile_practice.py) | 由 kernprof 提供 @profile，观察逐行耗时；不能直接假定普通 Python 提供该装饰器。 |
| [memory_practice.py](memory_practice.py) | tracemalloc 快照与分配行排名。 |
| [rss_memory_practice.py](rss_memory_practice.py) | memory_profiler 观察引用、del 与进程 RSS。 |
| [gpu_memory_practice.py](gpu_memory_practice.py) | 区分 allocated、reserved 与空闲缓存清理。 |
| [tensorboard_practice.py](tensorboard_practice.py) | 当前保存 lr=1.1 的发散实验，初始 w=3、目标值 5、20 次更新。 |
| [vscode_debug_practice.py](vscode_debug_practice.py) | 在 backward 与 optimizer.step 前后用 F10 和调试控制台检查数值。 |
| [debug_tools_fault_practice.py](debug_tools_fault_practice.py) | 教材工具的故障副本，在 demo_nan_detection 中故意将前向输出除以零；不是修复后的训练代码。 |

教材参考脚本保留原样。故障副本除目标注入外，包含编辑器产生的空行和表达式格式调整。

## 已核验的调试与性能实验

- 张量结构：shape=(2, 3)、float32、CPU；插入 NaN 后 shape/dtype/device 不变，min/max/mean 变为 NaN，说明结构信息不足以判断数值正常。
- pdb：模拟损失 0.5、150、NaN；在 step=1、2 暂停，暂停时 finished step 对应语句尚未执行。用 c 继续运行。
- 日志：INFO 级别记录三种消息；普通 print 不写入 FileHandler。即使 ERROR 消息写着“停止训练”，后续 print 仍会执行。
- 分段计时：模拟数据加载约 0.2005 秒，前向约 0.0504 秒，优先调查占用更多时间的加载部分。
- cProfile：三次 train_step 累计约 0.756 秒；load_data 约 0.604 秒、forward_pass 约 0.151 秒。cumtime 包括被调用函数，tottime 排除子调用。
- line_profiler：load_data 总耗时约 0.7567 秒；模拟读取数据的第一条 sleep 约占 79.4%，预处理 sleep 约占 19.9%。@profile 装饰函数不会因此自动调用函数。

这些时间是当时的演示测量，不是硬件基准；计时区间、并发与 GPU 异步执行都会影响解释。

## 内存与引用实验

- tracemalloc：在分配之前 start，1,000,000 字节的 bytearray 排在 100,000 字节之前；快照统计当时仍被跟踪的活跃分配，不能追溯 start 之前的分配。
- backup = large 只增加同一对象的引用，不复制数组。del large 删除该名字的引用；backup 保留对象时，内存仍属于该对象。删除最后一个引用后，对象才具备释放条件；进程 RSS 是否立即下降还受分配器影响。
- RSS：20,000,000 字节的 bytearray 使当时进程约从 26.3 MiB 增至 45.4 MiB；赋予 backup 和 del large 没有再次分配或释放这一份数据，del backup 后回落约 19.1 MiB。
- GPU：10,000,000 个 float32 元素约占 38.1 MiB；删除最后引用后 allocated 回到接近零，reserved 仍约 40 MiB；empty_cache 后 reserved 回落。
- reserved 包含正在使用的部分和未使用缓存；empty_cache 释放空闲缓存，不能替代删除活跃张量的引用。
- 教材工具中 tracemalloc 报告的 8864 B、80 B 不能解释为全部 PyTorch 张量存储。GPU 大张量演示 allocated 从约 0 增至 400.6 MB，清理后回到约 0；MB 与 MiB 不混用。

## 课内补学的 PyTorch 基础

以下小实验主要通过临时终端代码运行，没有分别保存为完整脚本。

- 设备：x.to("cuda") 跨设备返回 GPU 张量；原 x 仍是 CPU，赋回 x 才改变该名字指向的张量。device 是属性，创建时可传 device="cuda"。
- 索引和标量：二维张量索引从 0 开始；x[0, 1] 是第一行第二列。mean 返回标量张量，item 返回普通 Python 数值。
- 自动求导：w=3、loss=(w-5)**2 时，loss=4、梯度为 -4；backward 计算并累积梯度，不更新 w。
- SGD：lr=0.1 更新后 w 约为 3.4；重新计算损失约为 2.56。两轮不清零的梯度为 -4、-8；每轮清零则为 -4、-4。grad 是属性，不是方法。
- 梯度累积可支持多次反向传播后统一更新；是否需要平均取决于损失缩减与批次权重，不能一概累加后当作同样的学习率。
- detach 返回脱离原计算历史的结果，适合记录张量或明确停止某条梯度路径；并非所有张量都应 detach，也不因此复制底层数据。
- Linear(3, 2) 把每个样本的三个特征映射为两个特征。输入不求梯度时，输出仍可因为可训练参数而 requires_grad=True。
- 层间形状：先得到 (4, 2)，再送入要求三个输入特征的层会报错；学习者改为接收两个特征后得到 (4, 1)。
- forward hook 在模块前向计算后调用；remove 后不再打印。no_grad 中仍执行前向与 hook，但不为这些运算构建求导历史。
- 有限损失不保证有限梯度：w=0、loss=sqrt(w) 时，损失为 0，梯度为 Inf。应在本轮 backward 后、step 前检查梯度的有限性。

学习者表示能根据结果理解代码，但 API 的独立复写仍需后续练习；未据此宣称已能独立编写完整训练系统。

## TensorBoard 与可视化断点

- 学习者安装 TensorBoard 2.21.0 并看到曲线；事件目录为 WSL 的 /tmp/course-00-12-tensorboard/lr_01 与 lr_11。
- lr_01：lr=0.1，w 从 3 接近 5，损失下降；step=1 的原始值为 w 约 3.4、loss 约 2.56。
- lr_11：lr=1.1，第一次更新 w=7.4、重算损失 5.76；后续 w 在 5 两侧来回变化，距离扩大，损失上升。
- 两种实验均在每次 optimizer.step 之前记录 w 和 loss。当前脚本保留 lr_11；复现 lr_01 时需同时把 SGD 的 lr 改为 0.1、写入目录改为 lr_01。
- 页面核验：选中两个 run，Smoothing=0.6；每个实验同时显示浅色原始线和深色平滑线，共四条线。Value 是原始值，Smoothed 是显示用的平滑值。
- 未安装 TensorFlow 的 reduced feature set 提示未妨碍本次 PyTorch 标量查看；fast loading 指事件日志读取机制，现有曲线正常，本课未为此修改安装或服务配置。
- 直方图只做概念讲解，没有实际写入 add_histogram 日志。参数值接近零不等于梯度消失，要查看实际梯度及更新情况；正常收敛也可能导致梯度很小。
- VS Code：学习者在 loss.backward 行设断点，报告 3.0、4.0、None；F10 执行 backward 后 w 不变、w.grad 为 tensor(-4.)；再执行 step 后报告约 3.4、旧 loss=4.0、重新计算的 loss 约 2.56。
- 旧 loss 保存已计算出的结果，不会因为参数变化自动重新求值；浮点数尾差不是此处训练逻辑错误。

## 综合脚本与故障注入

- 教材 debug_tools.py 完整运行，终端出现 All demos complete。
- 正常损失 2.4247，NaN 检查为 False；人为 NaN 标量触发 True。CPU/GPU 混用时打印 MISMATCH，是预设的检测演示。结构化日志中的训练成绩也是固定消息，不是一次真实训练的成绩。
- 故障副本只在 demo_nan_detection 的前向输出处加入除零。学习者提供的 VS Code 输出显示 step=0 损失为 NaN，0.weight、0.bias、2.weight、2.bias 四组梯度均出现 NaN，检测返回 True。
- step=99 的 fake_nan_loss 与模型计算图独立；此处没有再次 backward。检测器打印的是上一次留下的 NaN 梯度，不能解读为 fake_nan_loss 又计算出了这些梯度。
- Normal loss 是固定打印标签，标签本身不能证明数值正常。原 detect_nan 仅在损失为 NaN 时检查梯度，不能替代独立的 isfinite 检查。

## 概念纠正与测验讲评

- 原题 1 选 B：数据泄漏是值得检查的候选，包括划分重叠、标签进入特征、先用全量数据拟合预处理统计量。但 99% 准确率本身不证明泄漏；两个集合都缺少同一条数据属于覆盖问题，也不自动构成泄漏。
- 原题 2 选 C：本课模拟负载确实由数据加载占主要时间。课程将其描述为“最常见”并给出比例，但没有提供统计来源；真实程序必须测量，不能假定 DataLoader 增加进程数必然加速。
- 原题 3 选 D：检查参数梯度、在故障点使用断点，有助于定位数值异常；还应检查输入、输出、损失和首次产生非有限值的运算。
- 训练集用于参数更新，验证集用于监控、调参和选择模型，测试集用于选定模型后的最终评估。反复根据测试集结果修改模型会使评估失去独立性。
- 在训练损失 0.8、0.4、0.2，验证损失 0.9、0.5、0.7 的假设表格中，学习者正确选择第二轮，并将第三轮描述为有过拟合风险。单次验证损失上升不充分证明过拟合。

## 实践边界与下一课

- TensorBoard 标量实验没有真实训练集/验证集划分，只验证这个人为目标函数的优化过程；过拟合通过概念和表格判断，未实际运行验证集训练。
- 环境操作由学习者执行；本课手动安装了 line_profiler、memory_profiler 与 TensorBoard。uv 的 copy 模式用于本课安装，没有据此声称已持久配置 UV_LINK_MODE。
- 临时性能报告、TensorBoard 事件日志在 WSL /tmp；logging_info.log、虚拟环境及缓存不纳入提交。/tmp 目录可能被清理，源码可用于重新生成演示结果。
- 可参考课程的[诊断提示模板](../../phases/00-setup-and-tooling/12-debugging-and-profiling/outputs/prompt-debug-ai-code.md)组织错误、形状、设备和数值证据；其中固定阈值与现象到根因的对应关系是排查线索，应验证后再采用修复。
- 下一课：00/13 Python for AI Engineering。先做两道本课回忆题，再按约定核对、保存并在聊天完整交付新课中文教材；后续需让学习者逐渐独立复写小段 Python/PyTorch 代码。
