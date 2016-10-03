#!/usr/bin/env python
# -*- coding: utf-8-*-
import os
import hashlib
import argparse
import sys
import time


def CheckSystem():
    if sys.platform != 'linux2':
        os.system("cls")
    else:
        os.system("clear")


def banner():
    print """	\033[1;32m
	 ____             _   _   _           _     
	| __ ) _ __ _   _| |_| | | | __ _ ___| |__  
	|  _ \| '__| | | | __| |_| |/ _` / __| '_ \ 
	| |_) | |  | |_| | |_|  _  | (_| \__ \ | | |
	|____/|_|   \__,_|\__|_| |_|\__,_|___/_| |_|\033[0m
 	    			     \033[0;35mBy: Pedro Souza \033[0m
 	\033[0;37mmd5, sha1, sha224, sha256, sha384, sha512\033[0m
 	Use python BruteHash --h para mais informações... 
	"""
    time.sleep(1)
ajuda = """
	Use o tipo de Hash que vai ser feita o brute força... e o caminho da WordList..
	Exemplo: python BruteHash.py --Tipo md5 --Hash 38e2b2e31c0fce9537f735dda9fdf10a --WordList /home/user/word.txt"
	--Tipo <<--- Comando para definir o tipo de Hash que é, md5, sha1, sha224, sha256, sha384, sha512 uma dessas.
	--Hash a palavra encriptada.
	--WordList o caminho da sua WordList. 
"""
CheckSystem()
banner()
parser = argparse.ArgumentParser()
parser.add_argument("--Tipo", action="store", dest="tipo",
                    help="Defina o tipo de Hash que deseja quebrar. MD5, SHA1, SHA224, SHA256, SHA384, SHA512 alguma dessas...", required=True)
parser.add_argument("--WordList", action="store", dest="WordList",
                    help="Caminho da WordList que será usada.", required=True)
parser.add_argument("--Hash", action="store", dest="Hash",
                    help="Tipo de Hash a ser realizada o Brute Force.", required=True)
parser.add_argument("--h", help="Opção de Ajuda", action="store_true")
args = parser.parse_args()
tipo = None
Hash = str(args.Hash)
if args.tipo.lower() == 'md5':
    tipo = hashlib.md5
elif args.tipo.lower() == 'sha1':
    tipo = hashlib.sha1
elif args.tipo.lower() == 'sha224':
    tipo = hashlib.sha224
elif args.tipo.lower() == 'sha256':
    tipo = hashlib.sha256
elif args.tipo.lower() == 'sha384':
    tipo = hashlib.sha384
elif args.tipo.lower() == 'sha512':
    tipo = hashlib.sha512
a = open(args.WordList, "r").readlines()
for kay in a:
    kay = kay.replace("\n", "").replace("\r", "")
    print "\033[0;31mPalavra a ser testada: " + str(kay) + "\033[0m"
    encripted = tipo(kay).hexdigest()
    if encripted == Hash:
        time.sleep(3)
        CheckSystem()
        banner()
        print "\033[0;32mHash original: " + str(args.Hash) + "\033[0m"
        print "\033[0;32mTexto original: " + str(kay) + "\033[0m"
        quit()
