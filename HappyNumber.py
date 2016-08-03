#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def Happy(number):
    fixo = number
    while 1:
        number = list(str(number))
        number1 = 0
        for i in number:
            number1 += int(i) ** 2
        number = number1
        if len(str(number1)) == 1 and int(number1) == 1:
            print(str(fixo) + " É feliz.")
            quit()
        if fixo == number1:
            print(str(fixo) + " Não é feliz. :/")
            quit()
Happy(7)  # Altere o número aqui para saber se é feliz ou não...
