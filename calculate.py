#!/usr/bin/env python
# -*- coding:utf-8 -*-
from math import sqrt, pi


class Calcular:
    def __init__(self, n1, n2):
        self.description = "Shit of Calculator."
        self.n1 = n1
        self.n2 = n2

    def soma(self):
        return self.n1 + self.n2

    def dividir(self):
        return self.n1 / self.n2

    def multiplicar(self):
        return self.n1 * self.n2

    def subtrair(self):
        return self.n1 - self.n2

    def potencia(self):
        return self.n1 ** self.n2

    def raiz(self):
        return sqrt(self.n1)

    def pi(self):
        return pi

calc = Calcular(10, 2)
print(calc.soma())
print(calc.dividir())
print(calc.multiplicar())
print(calc.subtrair())
print(calc.potencia())
print(calc.raiz())
print(calc.pi())
