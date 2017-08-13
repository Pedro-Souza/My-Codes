#-*- coding: utf-8 -*-
from time import sleep

cont = 6
result = 0

while 1:
    div = int(cont / 2)
    for i in range(1, div+1):
        if cont % i == 0:
            result += i
        else:
            result += 0
    if result == cont:
        print('Número perfeito => ' + str(result))
    cont += 1
    result = 0



