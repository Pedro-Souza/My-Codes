#!/usr/bin/env python
# -*- coding:utf-8 -*-

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


class GitHub():

    def GetRepos(self, user):
        self.msg = ""
        req = loads(get('https://api.github.com/users/' +
                        user + '/repos').text)
        self.msg += '\nRepositorys of user.'
        for i in range(len(req)):
            self.msg += '\n\nName repository: ' + str(req[i]['name'])
            self.msg += '\nDescription repository: ' + \
                str(req[i]['description'])
            self.msg += '\nURL repository: ' + str(req[i]['html_url'])
            self.msg += '\nStars: total: ' + \
                str(req[i]['stargazers_count'])
            self.msg += '\nForks total: ' + \
                str(req[i]['forks_count'])
        return self.msg

    def GetInfo(self, user):
        self.msg = ""
        req = loads(get('https://api.github.com/users/' + user).text)
        self.msg += '\nInformation of user:'
        self.msg += '\nName: ' + str(req['name'])
        self.msg += '\nEmail: ' + str(req['email'])
        self.msg += '\nCompany: ' + str(req['company'])
        self.msg += '\nBlog: ' + str(req['blog'])
        self.msg += '\nBio: ' + str(req['bio'])
        self.msg += '\nLocation: ' + str(req['location'])
        self.msg += '\nPublic repository: ' + str(req['public_repos'])
        self.msg += '\nFollowers: ' + str(req['followers']) + '\n'
        return self.msg


def Arguments():
    parser=ArgumentParser()
    parser.add_argument('--repos', dest='repos', action='store_true',
                        help='List all repository.')
    parser.add_argument('--user', dest='user', action='store',
                        required=True, help='Parameter for set user.')
    parser.add_argument('--info', dest='info', action='store_true',
                        help='Parameter for to get info of user')
    parser.add_argument('--all', dest='all', action='store_true',
                        help='Parameter for to define all options')
    args=parser.parse_args()
    if args.user and args.info:
        GetInfo(args.user)
    elif args.user and args.repos:
        GetRepos(args.user)
    elif args.user and args.all:
        GetInfo(args.user)
        GetRepos(args.user)
    else:
        print('Use --info, --repos or --all.')
