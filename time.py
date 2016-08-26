from time import time


class Time:
    def __init__(self):
        self.descrii = "simple test of time."

    def Test(self, dure=10000):
        for i in range(dure):
            print(i)


init = time()
ins = Time()
ins.Test()
fim = time()
print(fim - init)
