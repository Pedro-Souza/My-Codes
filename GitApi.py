#!/usr/bin/env python
# -*- coding:utf-8 -*-

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
    req = loads(get('https://api.github.com/users/' + user + '/repos').text)
    for i in range(len(req)):
        print('Name repository: ' + req[i]['name'])
        print('Description repository: ' + str(req[i]['description']))
        print('URL repository: ' + req[i]['html_url'])
        print('Stars: total: ' + str(req[i]['stargazers_count']))
        print('Forks total: ' + str(req[i]['forks_count']) + '\n')
        sleep(4)


def Arguments():
    parser = ArgumentParser()
    parser.add_argument('--repos', dest='repos', action='store_true',
                        help='List all repository.')
    parser.add_argument('--user', dest='user', action='store_true',
                        required=True, help='Parameter for set user.')
    parser.add_argument('--info', dest='info', action='store_true',
                        help='Parameter for to get info of user')
    parser.add_argument('--all', dest='all', action='store_true',
                        help='Parameter for to define all options')
    args = parser.parse_args()
    print(args.user)
    if args.user and args.info:
        GetInfo(args.user)
    elif args.user and args.repos:
        GetRepos(args.user)
    elif args.user and args.all:
        GetInfo(args.user)
        GetRepos(args.user)
    else:
        print('User --info, --repos or --all.')


def GetInfo(user):
    req = loads(get('https://api.github.com/users/' + user).text)
    print('Name: ' + req['name'])
    print('Company' + req['company'])
    print('Blog: ' + req['blog'])
    print('Bio: ' + req['bio'])
    print('Location: ' + req['location'])
    print('Email: ' + req['email'])
    print('Public repository: ' + str(req['public_repos']))
    print('Followers: ' + str(req['followers']))


Arguments()
