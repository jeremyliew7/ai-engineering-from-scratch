import torch

w = torch.tensor(3.0, requires_grad=True)
optimizer = torch.optim.SGD([w], lr=0.1)

optimizer.zero_grad()
loss = (w - 5) ** 2
loss.backward()
optimizer.step()

print("更新后的 w:", w.item())
