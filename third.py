import tkinter, datetime


def updateClock():
    stringvar.set(str(datetime.datetime.now())[11:19])
    window.after(5, updateClock)

clock = str(datetime.datetime.now())[11:19]

window = tkinter.Tk()

window.title("Clock")

window.geometry("600x200")
window.configure(bg="white")


window.after(5, updateClock)


stringvar = tkinter.StringVar(value=clock)

label1 = tkinter.Label(
    window,
    font=("Comic Sans", 40),
    bg="white",
    fg="orange"
)

label1.configure(textvariable=stringvar)

label1.pack()

window.mainloop()