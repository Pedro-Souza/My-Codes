#!/usr/bin/env python
# -*- coding:utf-8 -*-


fat = lambda n: n * fat(n - 1) if n > 1 else 1
print(fat(5))
