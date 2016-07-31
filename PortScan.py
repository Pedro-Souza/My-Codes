#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from sys import platform
from os import system
import socket

def System():
    if sys.platform in ['linux', 'linux2']:
        os.system("clear")
    else:
        os.system("cls")

def Connection(ip, port):
	print("1")
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ip,int(port)))
	print("2")
	if result == 0:
		print("Port open: "+ port)
	else:
		print("Prot close: "+ port)
	sock.close()

def Arguments():
	host = sys.argv[2].replace("http://", "").replace("https://", "").replace("www.", "")
	host = socket.gethostbyname(host)
	if sys.argv[3] == "--all": #Bug aqui, porém o sono é maior...
		for port in range(20,65535):
			Connection(host, port)
	elif sys.argv[3] == "--port":
		Connection(host, sys.argv[4])
Arguments()