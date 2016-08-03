#!/usr/bin/env python

from time import sleep
from requests import get
from json import loads
from sys import platform
from os import system


def Sistema():
    if platform in ['linux', 'linux2']:
        system("clear")
    else:
        system("cls")


def GetInfo(user):
    req = get("https://api.github.com/users/" + user + "/repos").text
    req = loads(req)
    for i in range(len(req)):
        print('Name repository: ' + req[i]['name'])
        print('Description repository: ' + str(req[i]['description']))
        print('URL repository: ' + req[i]['html_url'] + '\n')
        sleep(4)
GetInfo()
