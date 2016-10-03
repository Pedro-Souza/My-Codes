#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import urllib
import re
import argparse
import sys
os.system("clear")


def pesquisa(link):
    link = 'https://www.bing.com/search?' + urllib.urlencode({'q': link})
    read = urllib.urlopen(link).read()
    Addon, Addon1, counter = [], [], 0
    for line in re.findall('<h2><a href="(.*?)"', read):
        if 'msn' in line or 'FORM=EWRE' in line or 'wordpress.org' in line:
            pass
        else:
            Addon.append(line)
    for test in Addon:
        if len(Addon1) == 3:
            pass
        else:
            Addon1.append(test)
    for Gamer in Addon1:
        print "\033[1;35m" + str(Gamer) + "\033[0m"


def WordPress():
    os.system("clear")
    ReadWP = urllib.urlopen('http://www.wordpressexploit.com').read()
    find = re.findall('<font color="red">(.*?)</font></td>', ReadWP)
    if len(find) < 0:
        print len(find)
        print "\033[1;34mThere is no new vulnerabilities at the time.\033[0m"
        print "\033[0;\t32mEven more, made by Pedro Souza\033[0m"
        quit()
    for i in find:
        print "\033[0;31m" + str(i).replace('Published', '').encode("utf-8") + "\033[0m"
        print "--------------------------------------------------------------------------------------------"
        pesquisa(i.replace('Published', ''))
    print "\033[0;32\t\tmEven more, made by Pedro Souza\033[0m"


def Joomla():
    os.system("clear")
    ReadWP = urllib.urlopen('http://www.joomlaexploit.com').read()
    find = re.findall('<font color="red">(.*?)</font></td>', ReadWP)
    if len(find) < 0:
        print "\033[1;34mThere is no new vulnerabilities at the time.\033[0m"
        print "\033[0;32\t\tmEven more, made by Pedro Souza\033[0m"
        quit()
    for i in find:
        print "\033[0;31m" + str(i).replace('Published', '').encode("utf-8") + "\033[0m"
        print "------------------------------------------------------------------------"
        pesquisa(i.replace('Published', ''))
    print "\033[0;32\t\tmEven more, made by Pedro Souza\033[0m"
parser = argparse.ArgumentParser()
parser.add_argument(
    "--WordPress", help="To verify that the new vulnerabilities for WordPress", action="store_true")
parser.add_argument(
    "--Joomla", help="To verify that the new vulnerabilities for Joomla", action="store_true")
args = parser.parse_args()
if args.WordPress:
    WordPress()
elif args.Joomla:
    Joomla()
else:
    print "\033[0;37mUse -h for more information!\033[0m"
