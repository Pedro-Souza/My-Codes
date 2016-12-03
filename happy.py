#!/usr/bin/env python3
# -*-coding:utf-8 -*-



lista = []

class Happy(object):

    def getResp(self, number):
        lista.append(number)
        self.acc = 0
        for i in str(number):
            self.acc += int(i) ** 2
        if self.acc == 1:
            return True
        elif self.acc == lista[0]:
            return False
        else:
            Happy().getResp(self.acc)


a =  Happy().getResp(100)
