from tkinter import *


def teste():
    print(entrychiled.get())



class gui(object):
    def __init__(self):
        self.master = Tk()


    def crono(self):
        print("UÉ, TO AQUI.")

    def start(self):
        chield = Label(self.master, text='Tempo:').grid(row=0, column=0)
        input = Entry(self.master, textvariable=StringVar()).grid(row=0,
                                                        column=1)
        Button(self.master, text='Cronometrar!', command=self.crono).grid(row=0,
                                                        column=2)
        mainloop()


gui().start()
