#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from os import system
from sys import platform, argv
from socket import gethostbyname


def main():
    Sistema()
    Resover()


def Sistema():
    if platform in ['linux2', 'linux']:
        system("clear")
    else:
        system("cls")


def Resover():
    if len(argv) < 3:
        print("Use python3 Pegip.py -h <host>")
    else:
        print(len(argv))
        host = argv[2].replace(
            "https://", "").replace("http://", "").replace("www", "")
        print("IP: " + str(gethostbyname(host)))

main()
