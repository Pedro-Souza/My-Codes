#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import os
import re
os.system("clear")

ConecLer = urllib.urlopen('https://check.torproject.org/?lang=pt').read()
ip = re.findall('<strong>(.*?)</strong></p>', ConecLer)
text = re.findall('<p>(.*?) <strong>', ConecLer)
text2 = re.findall('<h1 class="off"> (.*?) </h1>', ConecLer)
for i in text:
    print i
for i in ip:
    print "\t\n\tIP: " + str(i)
