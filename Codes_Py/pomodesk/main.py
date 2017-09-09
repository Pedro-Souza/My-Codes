from tkinter import *


class gui(object):
    def __init__(self):
        self.master = Tk()


    def crono(self):
        pass

    def start(self):
        self.master.title('PomoDesk')
        self.time = StringVar()
        self.chield = Label(self.master, text='Tempo:').grid(row=0, column=0)
        self.input = Entry(self.master, textvariable=self.time).grid(row=0,
                                                        column=1)
        Button(self.master, text='Cronometrar!', command=self.crono).grid(row=0,
                                                        column=2)
        mainloop()


gui().start()
