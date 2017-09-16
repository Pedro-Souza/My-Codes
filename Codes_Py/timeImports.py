from time import time

a = time()
from os import system
b = time()
print(b-a)

c = time()
from os import *
d = time()
print(d-c)