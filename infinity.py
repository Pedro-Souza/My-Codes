#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import system
from sys import platform
from itertools import permutations


def System():
    if platform in ['linux', 'linux2']:
        system('clear')
    else:
        system('cls')

# In construction...


def Infinity(word):
    if "/" in word:
        word = word.split("/")
        words = ""
        for i in word:
            words += i
    else:
        words = word
    arq = open("WordList.txt", "w", closefd=True)
    for combinations in permutations(words):
        arq.write("".join(combinations) + "\n")


Infinity("Pedro")
