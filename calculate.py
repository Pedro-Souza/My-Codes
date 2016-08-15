#!/usr/bin/env python
# -*- coding:utf-8 -*-
from math import sqrt, pi


class Calcular:
    def __init__(self, n1, n2):
        self.description = "Shit of Calculator."
        self.n1 = n1
        self.n2 = n2

    def Soma(self):
        return self.n1 + self.n2

    def Dividir(self):
        return self.n1 / self.n2

    def Multiplicar(self):
        return self.n1 * self.n2

    def Subtrair(self):
        return self.n1 - self.n2

    def Potencia(self):
        return self.n1 ** self.n2

    def Raiz(self):
        return sqrt(self.n1)

    def Pi(self):
        return pi

calc = Calcular(10, 2)
print(calc.Soma())
print(calc.Dividir())
print(calc.Multiplicar())
print(calc.Subtrair())
print(calc.Potencia())
print(calc.Raiz())
print(calc.Pi())
