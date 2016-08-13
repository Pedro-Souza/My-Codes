#!/usr/bin/env python
# -*- coding:utf-8 -*-


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


calculator = Calcular()
print(calculator.Dividir(1, 2))
