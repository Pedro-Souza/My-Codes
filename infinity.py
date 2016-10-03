#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import system
from sys import platform
from itertools import permutations
from sys import argv


def System():
    if platform in ['linux', 'linux2']:
        system('clear')
    else:
        system('cls')


def Arguments():
    if len(argv) < 2:
        System()
        print("Please use --word 'Word Here'")
        print("Use / for to separate two words")
        quit()
    else:
        Infinity(argv[2])


def Infinity(word):
    System()
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
    print("Congratulations, WordList created successfully.")
    print("Name of file: WordList.txt")


Arguments()
