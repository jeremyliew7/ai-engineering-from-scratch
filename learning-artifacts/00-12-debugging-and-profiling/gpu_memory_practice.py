import torch

if not torch.cuda.is_available():
    raise SystemExit("CUDA 不可用")

def show(label):
    a = torch.cuda.memory_allocated() / 2**20
    r = torch.cuda.memory_reserved() / 2**20
    print(f"{label}: allocated={a:.1f} MiB, reserved={r:.1f} MiB")

show("初始")
x = torch.empty(10_000_000, device="cuda", dtype=torch.float32)
show("创建张量")
del x
show("删除引用")
torch.cuda.empty_cache()
show("清理空闲缓存")
