#!/usr/bin/env python3
#-*- coding=utf-8 -*-

from os import system, name
from random import randint
#from subprocess import Pipe

New_Mac, R, W, D = "", "\033[31m", "\033[38m", "\033[0m"


def Banner():
    print(R + """
				#   _______            ____    ____                 #
				#  |_   __ \          |_   \  /   _|                #
				#    | |__) |   ,--.    |   \/   |   ,--.   .---.   #
				#    |  __ /   `'_\ :   | |\  /| |  `'_\ : / /'`\]  #
				#   _| |  \ \_ // | |, _| |_\/_| |_ // | |,| \__.   #
				#  |____| |___|\'-;__/|_____||_____|\'-;__/'.___.'    #
				#                                                   #
	""" + D)


def main():
    global R, W, D
    if name == "nt":
        system("cls")
        Banner()
        print("[+] Script Desenvolvido para plataformas Linux. Em breve atualizações para multplataforma! [+]")
    else:
        system("clear")
    Banner()
    Generation()


def Generation():
    global New_Mac
    for i in range(6):
        New_Mac += "0123456789"[randint(0, 10)]  # Sorteia os numeros
        New_Mac += "abcdef"[randint(0, 5)]  # Sorteia as letras
        if i < 5:
            New_Mac += ":"
        else:
            pass
    print(R + "You new mac: " + D, New_Mac)


def Renovar(mac):


main()
