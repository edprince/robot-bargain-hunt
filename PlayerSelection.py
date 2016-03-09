from tkinter import *
import tkinter

top = tkinter.Tk()
PlayerVar1 = IntVar()
PlayerVar2 = IntVar()
P1 = Checkbutton(top, text = "Player 1", variable = PlayerVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
P2 = Checkbutton(top, text = "Player 2", variable = PlayerVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
P1.pack()
P2.pack()
top.mainloop()
