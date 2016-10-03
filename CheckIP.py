#!/usr/bin/python
# -*- coding:utf-8 -*-

from re import findall
from requests import get


ConecLer = get('https://check.torproject.org/?lang=pt').text
ip = findall('<strong>(.*?)</strong></p>', ConecLer)
text = findall('<p>(.*?) <strong>', ConecLer)
text2 = findall('<h1 class="off"> (.*?) </h1>', ConecLer)
for i in text:
    print(i)
for i in ip:
    print("\t\n\tIP: " + str(i))
