#!/usr/bin/env python
# -*- coding:utf-8 -*-
from os import system
from sys import platform


def CheckSystem():
    if platform == 'linux2':
        system("clear")
    else:
        system("cls")
CheckSystem()


def Encrypt(Word):
    lista, lista1 = [], []
    for encry in Word:
        lista.append(ord(encry) + 3)
    for krl in lista:
        lista1.append(chr(krl))
    print("\033[1;34mWord Encriptada: %s" % ''.join(lista1) + "\033[0m")


def Decrypt(Word):
    lista, lista1 = [], []
    for decry in Word:
        lista.append(ord(decry) - 3)
    for krl in lista:
        lista1.append(chr(krl))
    print("\033[1;34mWord Decryptada: %s" % ''.join(lista1) + "\033[0m")


def main():
    Word = raw_input("\033[0;31mWord: \033[0m")
    Verify = raw_input("\033[1;32m1 for Decrypt | 2 for Encrypt: \033[0m")
    if int(Verify) == 1:
        Decrypt(Word)
    elif int(Verify) == 2:
        Encrypt(Word)
    else:
        print("\033[1;32mUse 1 or 2!\033[0m")
main()
