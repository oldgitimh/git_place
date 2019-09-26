import time


class TimeSum(object):
    def __init__(self):
        self.time = 0
        self.run_time = 0

    def __enter__(self):  # 当进入with语句时，调用它获取资源
        self.time = time.time()
        return self  # 返回一个类

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.run_time = float(time.time() - self.time)

    def time_print(self):
        print(f'code running Time:{self.run_time:.2f}s')