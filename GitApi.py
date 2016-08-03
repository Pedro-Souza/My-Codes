#!/usr/bin/env python

from time import sleep
from requests import get
from json import loads
from sys import platform
from os import system
from argparse import ArgumentParser


def Sistema():
    if platform in ['linux', 'linux2']:
        system("clear")
    else:
        system("cls")


def GetRepos(user):
    req = get("https://api.github.com/users/" + user + "/repos").text
    req = loads(req)
    for i in range(len(req)):
        print('Name repository: ' + req[i]['name'])
        print('Description repository: ' + str(req[i]['description']))
        print('URL repository: ' + req[i]['html_url'])
        print('Stars: total: ' + str(req[i]['stargazers_count']))
        print('Forks total: ' + str(req[i]['forks_count']) + '\n')
        sleep(4)


def Arguments():
    parser = ArgumentParser()
    parser.add_argument('--repos', dest='repos',
                        action='store', help="List all repository.")
    parser.add_argument('--user', dest='user', action='store',
                        required=True, help='Parameter for set user.')
    parser.add_argument('--info', dest='info', action='store',
                        help='Parameter for to get info of user')


def GetInfo():
    # in construction.
    pass


GetRepos('GouveaHeitor')
