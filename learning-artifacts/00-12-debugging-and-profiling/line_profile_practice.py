import time

@profile
def load_data():
    time.sleep(0.20)  # 模拟读取数据
    data = [1., 2., 3.]
    time.sleep(0.05)  # 模拟预处理
    return data

for _ in range(3):
    load_data()
