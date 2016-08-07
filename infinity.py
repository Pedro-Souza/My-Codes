#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import system
from sys import platform


def System():
    if platform in ['linux', 'linux2']:
        system('clear')
    else:
        system('cls')

# In construction...
