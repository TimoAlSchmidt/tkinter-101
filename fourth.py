import tkinter,random
from tkinter import ttk
from tkinter.messagebox import showinfo

items = ["appel","banaan","mandarijn","goud","schoen","sok","lader","telefoon"]

def grabItem():
    global items
    item = items.pop(items.index(random.choice(items)))
    if len(items) > 0:
        showinfo(title="Congratulation", message="Gefeliciteerd, je hebt een {} gegrabbeld".format(item))
        stringvar.set("Er zijn nog {} item(s) in de grabbelton!".format(len(items)))
    else:
        showinfo(title="Congratulation", message="Gefeliciteerd, je hebt een {} gegrabbeld".format(item))
        stringvar.set("Er zijn geen items meer in de grabbelton!".format(len(items)))


window = tkinter.Tk()
button = tkinter.Button(window, text="Grabbelen", command=grabItem)

window.title("Grabbelen")

window.geometry("200x50")
window.configure(bg="white")

button.pack()

stringvar = tkinter.StringVar(value="Er zijn nog {} items in de grabbelton!".format(len(items)))

label1 = tkinter.Label(
    window,
    bg="white",
    fg="orange"
)

label1.configure(textvariable=stringvar)

label1.pack()

window.mainloop()