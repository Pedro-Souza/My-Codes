#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
from requests import get
from sys import platform


def Sistema():
    if platform != 'linux2':
        system("cls")
    else:
        system("clear")


def Banner():
    print("""\033[0;35m         ____        _     ____                  _             
        / ___| _   _| |__ |  _ \  ___  _ __ ___ (_)_ __   ___  
        \___ \| | | | '_ \| | | |/ _ \| '_ ` _ \| | '_ \ / _ \ 
         ___) | |_| | |_) | |_| | (_) | | | | | | | | | | (_) |
        |____/ \____|____/|____/ \___/|_| |_| |_|_|_| |_|\___/ \033[0m
     """)


def TesteSub(site):
    try:
        r = get(site)
        if r.status_code == 200:
            print("\033[0;31mSub existente: " + site + "\033[0m")
            pass
        else:
            print("\033[1;32mSub inesistente: " + site + "\033[0m")
    except:
        print("\033[1;32mSub inesistente: " + site + "\033[0m")


def Gambiarra(subs, site):
    if "www" in site:
        if site[:8] == "https://":
            site = site[:8] + subs + "." + site[12:]
            TesteSub(site)
        elif site[:7] == "http://":
            site = site[:7] + subs + "." + site[11:]
            TesteSub(site)
        else:
            print("User https:// ou http://")
    else:
        if site[:8] == "https://":
            site = site[:8] + subs + "." + site[8:]
            TesteSub(site)
        elif site[:7] == "http://":
            site = site[:7] + subs + "." + site[7:]
            TesteSub(site)
        else:
            print("Use https:// ou http://")


def Percorrer():
    lista = input("\033[0;34mEntre com a lista: \033[0m")
    site = input("\033[0;34mEntre com o site: \033[0m")
    print("-" * 125)
    lista = open(lista, "r").readlines()
    for i in lista:
        i = i.replace("\n", "").replace("\r", "")
        Gambiarra(i, site)
Sistema()
Banner()
Percorrer()
