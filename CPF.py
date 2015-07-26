#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Caso de erro na importação, o programa exibe uma mensagem. Assim auxilia o 
#usuário
try: import requests
except ImportError: print(" [-] \"requests\" é necessário!")

try: from bs4 import BeautifulSoup
except ImportError: print(" [-] \"BeautifulSoup\" é necessário!")

import re 
#Ja que demais funções do módulo não serão utilizadas, basta importar a funções
#específicas
from sys import platform
from os import system

#Defina variáveis para as cores. Assim, caso deseja trocar, facilita a vida
green = "\033[0;32m"
default = "\033[0m"

#Em Python 3, raw_input foi removido. Portanto apresentará erro. Caso aconteça,
#raw_input será atribuido o valor input. Assim você consegue uma aplicação que
#roda em Python 2 e 3
try:
	raw_input
except NameError:
	raw_input = input

#Em Python 3 "linux2" retornará False.
#Ao invés de detectar o Linux, pode apenas detectar o Windows e utilizar um else
#para demais sistemas (Linux, Cygwin, OSX)
def Sistema():
	if platform == "linux2" or platform == "linux":
		system("clear")
	elif platform == "win32":
		system("cls")
	else:
		pass
Sistema()

cpf = raw_input("CPF ")
req = requests.get('http://tudosobretodos.se/%s' % cpf)
soup = BeautifulSoup(req.content)

for i in soup.findAll('span', attrs={'class': 'textoTituloDetalhesPessoa'}):
	if i.text == cpf:
		print (green + "Não foi possível achar informações para esse CPF" + \
default)
		quit()
	
links = [] 
for i in soup.findAll('h1', attrs={'class': 'textoTituloDetalhesPessoa'}):
	print (green + "Nome: "+i.text+ default)

for i in soup.findAll('div', attrs={'class': 'innerDetalheDir'}):
	links.append(i.text)

sexo = links[0].replace("\t", "").replace("\n", "").replace("Adquira créditos \
para visualizar", "")

if "MASCULINO" in sexo:
	print (green + "Data de nascimento: " + sexo[9:] + default)
	print (gree + "Sexo: " + sexo[:9] + default)
else: 
	print (green + "Data de nascimento: " + sexo[8:] + default)
	print (green + "Sexo: "+ sexo[:8] + default)

print (green + "Bairro: "+ links[3].replace("\n", "").replace("\t", "") + default)
print (green + "Cidade: "+links[4].replace("\n", "").replace("\t", "") + default)
print (green + "Estado: "+links[5].replace("\n", "").replace("\t", "") + default)
print (green + "CEP: "+links[6].replace("\n", "").replace("\t", "") + default)

result = []
for i in soup.findAll('div', attrs={'class': 'itemMoradores'}):
	result.append(i.text)
if len(result) < 2:
	print (green + "Não foi possível pegar os nomes dos vizinhos" + default)
else:
	print (green + "Vizinho: "+result[0].replace("\t", "").replace("\n", "")+default)
	print (green + "Vizinho: "+result[1].replace("\t", "").replace("\n", "")+default)
	print (green + "Vizinho: "+result[2].replace("\t", "").replace("\n", "")+default)
	print (green + "Vizinho: "+result[3].replace("\t", "").replace("\n", "")+default)
	print (green + "Vizinho: "+result[4].replace("\t", "").replace("\n", "")+default)
