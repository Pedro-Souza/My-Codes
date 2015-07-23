#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import re 
from bs4 import BeautifulSoup
import os 
import sys

def Sistema():
	if sys.platform != "linux2":
		os.system("clear")
	else:
		os.system("cls")
Sistema()

cpf = input("CPF ")
req = requests.get('http://tudosobretodos.se/'+cpf)
soup = BeautifulSoup(req.content)

for i in soup.findAll('span', attrs={'class': 'textoTituloDetalhesPessoa'}):
	if i.text == cpf:
		print ("\033[0;32mNão foi possível achar informações para esse CPF\033[0m")	
		quit()
	
links = [] 
for i in soup.findAll('h1', attrs={'class': 'textoTituloDetalhesPessoa'}):
	print ("\033[0;32mNome: "+i.text+"\033[0m")

for i in soup.findAll('div', attrs={'class': 'innerDetalheDir'}):
	links.append(i.text)

sexo = links[0].replace("\t", "").replace("\n", "").replace("Adquira créditos para visualizar", "")


if "MASCULINO" in sexo:
	print ("\033[0;32mData de nascimento: "+sexo[9:]+"\033[0m")
	print ("\033[0;32mSexo: "+sexo[:9]+"\033[0m")
else: 
	print ("\033[0;32mData de nascimento: "+sexo[8:]+"\033[0m")
	print ("\033[0;32mSexo: "+ sexo[:8]+"\033[0m")

print ("\033[0;32mBairro: "+ links[3].replace("\n", "").replace("\t", "")+"\033[0m")
print ("\033[0;32mCidade: "+links[4].replace("\n", "").replace("\t", "")+"\033[0m")
print ("\033[0;32mEstado: "+links[5].replace("\n", "").replace("\t", "")+"\033[0m")
print ("\033[0;32mCEP: "+links[6].replace("\n", "").replace("\t", "")+"\033[0m")

result = []
for i in soup.findAll('div', attrs={'class': 'itemMoradores'}):
	result.append(i.text)
if len(result) < 2:
	print ("\033[0;32mNão foi possível pegar os nomes dos vizinhos\033[0m")
else:
	print ("\033[0;32mVizinho: "+result[0].replace("\t", "").replace("\n", "")+"\033[0m")
	print ("\033[0;32mVizinho: "+result[1].replace("\t", "").replace("\n", "")+"\033[0m")
	print ("\033[0;32mVizinho: "+result[2].replace("\t", "").replace("\n", "")+"\033[0m")
	print ("\033[0;32mVizinho: "+result[3].replace("\t", "").replace("\n", "")+"\033[0m")
	print ("\033[0;32mVizinho: "+result[4].replace("\t", "").replace("\n", "")+"\033[0m")
