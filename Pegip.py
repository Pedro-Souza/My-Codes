#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os
import sys
import socket


def main():
    Sistema()
    Resover()


def Sistema():
    if sys.platform in ['linux2', 'linux']:
        os.system("clear")
    else:
        os.system("cls")


def Resover():
    if len(sys.argv) < 3:
        print("Use python3 Pegip.py -h <host>")
    else:
        print(len(sys.argv))
        host = sys.argv[2].replace(
            "https://", "").replace("http://", "").replace("www", "")
        print("IP: " + str(socket.gethostbyname(host)))

main()
