# _*_ coding:utf-8 _*_
from os import system
system("clear")
# Formula V-A+F=2
print("Formula: V-A+F=2 ")


def valorF():
    # Faz o calculo para saber o valor de F
    B = (V - A) * -1
    F = B + 2
    print("O valor de F é: " + str(F) + ".")


def valorV():
    # Faz o calculo para saber o valor de V
    B = (A + F) * -1
    V = B + 2
    print("O valor de V é: " + str(V) + ".")
    # V-A+F=2


def valorA():
    # Faz o calculo para saber o valor de A.
    B = (V + F) * -1
    A = B + 2
    print("O valor de A é: " + str(A) + ".")


def op():
    res = str(input("Qual letra F-V-A? "))
    if res == 'F':
        valorF()
    elif res == 'V':
        valorV()
    elif res == 'A':
        valorA()
    else:
        print("Letra não encontrada.")

V = input("Valor de V: ")
A = input("Valor de A: ")
F = input("Valor de F: ")

if V < 1 or A < 1 or F < 1:
    print("Poliedro Não existe.")
else:
    op()
