#!/usr/bin/env python
# -*- coding:utf-8 -*-


import time

ini = time.time()

for i in range(0, 100):
    if (i % 2) == 0:
        print(str(i) + ' É par.')
    else:
        print(str(i) + ' É impar.')
fim = time.time()
print('Tempo de execução: ' + str(fim - ini))
