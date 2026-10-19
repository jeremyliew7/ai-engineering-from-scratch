import torch
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("/tmp/course-00-12-tensorboard/lr_11")
w = torch.tensor(3.0, requires_grad=True)
optimizer = torch.optim.SGD([w], lr=1.1)

for step in range(20):
    optimizer.zero_grad()
    loss = (w - 5) ** 2
    writer.add_scalar("loss/train", loss.item(), step)
    writer.add_scalar("parameter/w", w.item(), step)
    loss.backward()
    optimizer.step()

writer.close()
print("日志目录:", writer.log_dir)
