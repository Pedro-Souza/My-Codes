#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import os
import re
os.system("clear")
ip = input("\033[35mEntre com o IP: \033[0m")
loca = "http://www.localizarip.com.br/localizar-ip.php?ip=" + ip
abrir = urllib.urlopen(loca).read()
pais, estado, cidade, provedor = re.findall('Pa&iacute;s:<b>(.*?)</b><br>', abrir), re.findall(
    'Estado:<b>(.*?)</b><br>', abrir), re.findall('Cidade:<b>(.*?)</b><br>', abrir), re.findall('Provedor:<b>(.*?)</b><br>', abrir)
print "\033[0;32m\t\t\t\t\nDados...\033[0m"
for i in pais:
    print "\033[35m\tPaís: " + i + "\033[0m"
for i in estado:
    print "\033[35m\tEstado: " + i + "\033[0m"
for i in cidade:
    print "\033[35m\tCidade: " + i + "\033[0m"
for i in provedor:
    print "\033[35m\tProvedor: " + i + "\033[0m"
