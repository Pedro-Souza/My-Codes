#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sys import platform, argv
from os import system
from socket import socket


def System():
    if platform in ['linux', 'linux2']:
        system("clear")
    else:
        system("cls")


def Connection(ip, port, time=6):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(time)
    result = sock.connect_ex((ip, int(port)))
    if result == 0:
        print("Port open: " + str(port))
    else:
        print("Prot close: " + str(port))
    sock.close()


def Arguments():
    host = argv[2].replace(
        "http://", "").replace("https://", "").replace("www.", "")
    host = socket.gethostbyname(host)
    if argv[3] == "--all":
        for port in range(20, 65535):
            Connection(host, port)
    elif argv[3] == "--port":
        port = argv[4].split("-")
        for i in port:
            Connection(host, int(i))
if len(argv) < 3:
    System()
    print(
        "Use --host for to set the site, --port[22-43-80] for to set door or --all.")
    print("Exaple: python PortScan --host google.com --port 22-43-80")
    quit()
else:
    Arguments()
