#!/usr/bin/env python
# -*- coding:utf-8 -*-


a = 0
b = 1
num = int(input("Até qual número? "))
while b < num:
    a = b
    b = a + b
print(a, b)
