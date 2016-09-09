#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
from os import system
import sys
import argparse


def Banner():
    print """\033[0;32m 
		     _       _           _       _____ _           _           
	   	    / \   __| |_ __ ___ (_)_ __ |  ___(_)_ __   __| | ___ _ __ 
 	 	   / _ \ / _` | '_ ` _ \| | '_ \| |_  | | '_ \ / _` |/ _ \ '__|
 		  / ___ \ (_| | | | | | | | | | |  _| | | | | | (_| |  __/ |   
		 /_/   \_\__,_|_| |_| |_|_|_| |_|_|   |_|_| |_|\__,_|\___|_| \033[0m 
	"""


def Sistema():
    if sys.platform != "linux2":
        system("cls")
    else:
        system("clear")


def Argumentos():
    global args
    parse = argparse.ArgumentParser()
    parse.add_argument("-S", action="store", dest="S",
                       required=True, help="Use -s para definir o site.")
    parse.add_argument("-W", action="store", dest="W", required=True,
                       help="Use -W para passar o caminho da WordList.")
    args = parse.parse_args()
    print "\033[0;31m\nSite a busca: " + args.S
    print "WordList que está sendo usada: " + args.W + "\033[0m"
    print "\033[0;37m-" * 125 + "\n\033[0m"


def Conec(Word, site):
    Word = open(args.W, "r").readlines()
    for i in Word:
        i = i.replace("\n", "").replace("\r", "")
        abrir = urllib.urlopen(site + i)
        if abrir.getcode() == 200:
            abrir = abrir.read()
            if 'login' or 'senha' in abrir:
                print "\033[0;32mPossivel página de login: " + site + i + "\033[0m"
            else:
                print "\033[0;34mPágina não encontrada: " + site + i + "\033[0m"
        else:
            print "\033[0;34mPágina não encontrada: " + site + i + "\033[0m"


Sistema()
Banner()
Argumentos()
Conec(args.W, args.S)
