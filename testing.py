from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()

def var_states():
    print("Character 1: %d,\nCharacter 2: %d" % (var1.get(), var2.get()))

Label(top,text="Choose your character")

CharacterVar1 = IntVar()
CharacterVar2 = IntVar()
P1 = Checkbutton(top, text = "Character 1", variable = CharacterVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
P2 = Checkbutton(top, text = "Character 2", variable = CharacterVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 20)
P1.pack()
P2.pack()

ok=Menubutton (top, text="Ok",\
                height=1,\
                width =10)
ok.grid()

ok.pack() 

top.mainloop()
