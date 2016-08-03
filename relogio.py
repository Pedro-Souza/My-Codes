#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter
from time import strftime


def Gui():
    global gui
    gui = tkinter.Label()
    gui.pack()
    gui['text'] = strftime('%H:%M:%S')
    gui['font'] = 'Helvita 50 bold'
    gui['foreground'] = 'gray'
    gui['bg'] = 'red'
Gui()


def cont():
    agora = strftime('%H:%M:%S')
    if gui['text'] != agora:
        gui['text'] = agora
    gui.after(100, cont)
cont()
gui.mainloop()
