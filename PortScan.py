#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from sys import platform, argv
from os import system
import socket

def System():
    if platform in ['linux', 'linux2']:
        system("clear")
    else:
        system("cls")

def Connection(ip, port, time=6):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(time)
	result = sock.connect_ex((ip,int(port)))
	if result == 0:
		print("Port open: "+ str(port))
	else:
		print("Prot close: "+ str(port))
	sock.close()

def Arguments():
	host = argv[2].replace("http://", "").replace("https://", "").replace("www.", "")
	host = socket.gethostbyname(host)
	if argv[3] == "--all": #Bug aqui, porém o sono é maior...
		for port in range(20,65535):
			Connection(host, port)
	elif argv[3] == "--port":
		Connection(host, argv[4])
Arguments()