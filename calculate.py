#!/usr/bin/env python
# -*- coding:utf-8 -*-
from math import sqrt, pi, tan


class Calcular:
    def __init__(self):
        self.description = "Shit of Calculator."

    def Soma(self, n1, n2):
        return n1 + n2

    def Dividir(self, n1, n2):
        return n1 / n2

    def Multiplicar(self, n1, n2):
        return n1 * n2

    def Subtrair(self, n1, n2):
        return n1 - n2

    def Potencia(self, n1, n2):
        return n1 ** n2

    def Raiz(self, n):
        return sqrt(n)

    def Pi(self):
        return pi

    def Tan(self, n1):
        return tan(n1)

calculator = Calcular()
print(calculator.Raiz(9))
