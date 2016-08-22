from time import time
inicio = time()
for i in range(1, 10000):
    print(i)
fim = time.time()
print(fim - inicio)
