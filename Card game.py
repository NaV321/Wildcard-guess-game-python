from tkinter import *

import tkinter as tk

import tkinter.messagebox
 
# pip install pillow
from PIL import Image, ImageTk


c = ('Correct answer')
C = ('Correct You Can Go to next level')
h = ('It starts with M')
h1 = ('It starts with C')
w = ('Wrong Answer')
W = ('Try Again')
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("mango.png")
        load = load.resize((350, 300), Image.ANTIALIAS)
        
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=50)
def buttonClick():
     tkinter.messagebox.showinfo('Hint', h)
def buttonClick2():
    tkinter.messagebox.showinfo(w, W)
def buttonClick3():
    tkinter.messagebox.showinfo(c, C)
    root1.destroy()
   
    
def buttonClick4():
    tkinter.messagebox.showinfo(w, W)

    
   


def buttonClick1():
   
    tkinter.Button(root1, text='Apple',command=buttonClick2).place(x=540, y=120)
    tkinter.Button(root1, text='Mango',command=buttonClick3 ).place(x=540, y=150)
    tkinter.Button(root1, text='Orange',command=buttonClick4).place(x=540, y=180)

root1 = Tk()

app = Window(root1)
root1.wm_title("Guess What?? Level 1")
root1.geometry("800x400")
root1.resizable(False, False)
tkinter.Button(root1, text='Get a hint',command=buttonClick).place(x=740, y=50)
tkinter.Button(root1, text='Options',command=buttonClick1).place(x=740, y=20)   


root1.mainloop()

class Window1(Frame):
    def __init__(self, master1=None):
        Frame.__init__(self, master1)
        self.master = master1
        self.pack(fill=BOTH, expand=1)
        
        
        load1 = Image.open("cb.png")
        load1 = load1.resize((350, 300), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load1)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=50)
def buttonClicka():
     tkinter.messagebox.showinfo('Hint', h1)
def buttonClick2a():
    tkinter.messagebox.showinfo(c, C)
def buttonClick3a():
    tkinter.messagebox.showinfo(w, W)
    root2.destroy()
   
    
def buttonClick4a():
    tkinter.messagebox.showinfo(w, W)

    
   


def buttonClick1a():
   
    tkinter.Button(root2, text='Cowboy',command=buttonClick2a).place(x=540, y=120)
    tkinter.Button(root2, text='Pirate',command=buttonClick3a ).place(x=540, y=150)
    tkinter.Button(root2, text='Captain',command=buttonClick4a).place(x=540, y=180)
    
root2 = Tk()

app = Window1(root2)
root2.wm_title("Guess What?? Level 2")
root2.geometry("800x400")
root2.resizable(False, False)
tkinter.Button(root2, text='Get a hint',command=buttonClicka).place(x=740, y=50)
tkinter.Button(root2, text='Options',command=buttonClick1a).place(x=740, y=20)   

root2.mainloop()
class Window2(Frame):
    def __init__(self, master1=None):
        Frame.__init__(self, master1)
        self.master = master1
        self.pack(fill=BOTH, expand=1)
        
        
        load1 = Image.open("lily.png")
        load1 = load1.resize((350, 300), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load1)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=50)
def buttonClickab():
     tkinter.messagebox.showinfo('Hint', h1)
def buttonClick2ab():
    tkinter.messagebox.showinfo(c, C)
    root3.destroy()
def buttonClick3b():
    tkinter.messagebox.showinfo(w, W)
    
   
    
def buttonClick4ab():
    tkinter.messagebox.showinfo(w, W)

    
   


def buttonClick1ab():
   
    tkinter.Button(root2, text='Lily',command=buttonClick2ab).place(x=540, y=120)
    tkinter.Button(root2, text='China Rose',command=buttonClick3ab ).place(x=540, y=150)
    tkinter.Button(root2, text='Lotus',command=buttonClick4ab).place(x=540, y=180)
    
root3 = Tk()

app = Window2(root3)
root3.wm_title("Guess What?? Level 3")
root3.geometry("800x400")
root3.resizable(False, False)
tkinter.Button(root3, text='Get a hint',command=buttonClickab).place(x=740, y=50)
tkinter.Button(root3, text='Options',command=buttonClick1ab).place(x=740, y=20)   

root3.mainloop()



