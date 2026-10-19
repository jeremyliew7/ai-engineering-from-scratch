import torch

for step, value in enumerate([0.5, 150.0, float("nan")]):
    loss = torch.tensor(value)
    print("step:", step, "loss:", loss.item())

    if loss.item() > 100 or torch.isnan(loss):
        breakpoint()

    print("finished step:", step)
