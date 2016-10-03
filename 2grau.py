#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import sqrt


class Calculater:
    def __init__(self):
        self.descri = "Simple library for calculation operation of 2 degree."

    def calculate_x(self, delta, a, b):
        self.x_linha_first = (- b + sqrt(delta)) / 2 * a
        self.x_linha_second = (- b - sqrt(delta)) / 2 * a
        return self.x_linha_first, self.x_linha_second

    def delta_full(self, a, b, c):
        return self.calculate_x((((-b**2) * -1) - 4 * a * c), a, b)


degree = Calculater()
degree.delta_full(-1, 2, 3)
