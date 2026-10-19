import time

def load_data():
    time.sleep(0.20)
    return [1., 2., 3.]

def forward_pass(data):
    time.sleep(0.05)
    return sum(data)

def train_step():
    return forward_pass(load_data())

for _ in range(3):
    train_step()
