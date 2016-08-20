#!/usr/bin/env python
# -*- coding:utf-8 -*-


from time import time

ini = time()

for i in range(0, 100):
    if (i % 2) == 0:
        print(str(i) + ' É par.')
    else:
        print(str(i) + ' É impar.')
fim = time()
print('Tempo de execução: ' + str(fim - ini))
