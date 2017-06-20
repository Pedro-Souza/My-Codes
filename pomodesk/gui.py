from tkinter import *


def teste():
	print(e1.get())



master = Tk()

Label(master, text="First test").grid(row=0)
Label(master, text="test First").grid(row=0)



e1 = Entry(master).grid(row=0, column=1)
Button(master, text="Exibir texto" , command=teste)

mainloop()


