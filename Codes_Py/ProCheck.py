#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from os import name, system
from urllib2 import urlopen
from re import findall

# Cores que serão usadas no script.
D, R, G = "", "", ""
proxy = open("proxys.txt", "a")
ColetedProxy = []
ProxList = ['http://dogdev.net/Proxy/BR/r/Pernambuco', 'http://dogdev.net/Proxy/BR/r/S%25C3%25A3o%2BPaulo',
            'http://dogdev.net/Proxy/BR/r/Maranh%25C3%25A3o', 'http://dogdev.net/Proxy/BR/r/Minas%2BGerais',
            'http://dogdev.net/Proxy/BR/r/Rio%2BGrande%2Bdo%2BNorte', 'http://dogdev.net/Proxy/BR/r/Goi%25C3%25A1s',
            'http://dogdev.net/Proxy/BR/r/Amazonas', 'http://dogdev.net/Proxy/BR/r/Rio%2Bde%2BJaneiro',
            'http://dogdev.net/Proxy/BR/r/Cear%25C3%25A1', 'http://dogdev.net/Proxy/BR/r/Santa%2BCatarina',
            'http://dogdev.net/Proxy/BR/r/Paran%25C3%25A1', 'http://dogdev.net/Proxy/BR/r/Bahia',
            'http://dogdev.net/Proxy/BR/r/Mato%2BGrosso', 'http://dogdev.net/Proxy/BR/r/Alagoas',
            'http://dogdev.net/Proxy/BR/r/Par%25C3%25A1', 'http://dogdev.net/Proxy/BR/r/Para%25C3%25ADba',
            'http://dogdev.net/Proxy/BR/r/Distrito%2BFederal', 'http://dogdev.net/Proxy/BR/r/Esp%25C3%25ADrito%2BSanto',
            'http://dogdev.net/Proxy/BR/r/Piau%25C3%25AD', 'http://dogdev.net/Proxy/BR/r/Rio%2BGrande%2Bdo%2BSul',
            'http://dogdev.net/Proxy/BR/r/Mato%2BGrosso%2Bdo%2BSul', 'http://dogdev.net/Proxy/BR/r/Acre',
            'http://dogdev.net/Proxy/BR/r/Sergipe', 'http://dogdev.net/Proxy/BR/r/Rond%25C3%25B4nia',
            'http://dogdev.net/Proxy/BR/r/Amap%25C3%25A1', 'http://dogdev.net/Proxy/BR/r/Tocantins',
            'http://dogdev.net/Proxy/BR/r/Roraima', 'http://dogdev.net/Proxy/BR/r/Federal',
            'http://dogdev.net/Proxy/BR/r/Federal%2BDistrict']
Banner = """
		       ___             ___ _               _    
  		      / _ \_ __ ___   / __\ |__   ___  ___| | __
 		     / /_)/ '__/ _ \ / /  | '_ \ / _ \/ __| |/ /
		    / ___/| | | (_) / /___| | | |  __/ (__|   < 
		    \/    |_|  \___/\____/|_| |_|\___|\___|_|\_\ \n\n
    """


def Main():
    System()
    CatchProxys()


def System():
    global D, R, G, Banner
    if name == 'nt':
        system("cls")
        print(Banner)
    else:
        D, R, G = "\033[00m", "\033[31m", "\033[32m"
        system("clear")
        Banner = G + Banner + D


def CatchProxys():
    global ProxList, ColetedProxy, proxy
    for i in ProxList:
        print(R + "Coletando Proxy's" + D)
        html = urlopen(i).read()
        regex = findall('">(.*?)</a></td>', html)
        ColetedProxy = ColetedProxy + regex[1:]
        for i in regex[1:]:
            proxy.write(i + "\n")
    proxy.close()
    print(G + "Total de proxy coletado: " + str(len(ColetedProxy)) + D)

Main()
