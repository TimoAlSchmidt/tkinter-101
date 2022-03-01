import tkinter,random
from tkinter import ttk
from tkinter.messagebox import showinfo

colors = ["gray", "red", "green"]
num = 0

def changeWindow():
    global num
    if num == 0:
        window.configure(bg=colors[0])
    elif num < 0:
        window.configure(bg=colors[1])
    else:
        window.configure(bg=colors[2])

def goUp():
    global num
    num += 1
    stringvar.set(str(num))
    changeWindow()


def goDown():
    global num
    num -= 1
    stringvar.set(str(num))
    changeWindow()





window = tkinter.Tk()
up = tkinter.Button(window, text="Up", command=goUp)
down = tkinter.Button(window, text="down", command=goDown)

window.title("Clicker")

window.geometry("200x100")


stringvar = tkinter.StringVar(value=str(num))

label1 = tkinter.Label(
    window,
    bg="white",
    fg="orange"
)


label1.configure(textvariable=stringvar)

up.pack()
label1.pack()
down.pack()

window.mainloop()