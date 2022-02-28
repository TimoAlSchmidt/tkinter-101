import tkinter

window = tkinter.Tk()

colors = ["white", "yellow", "orange"]

window.title("Hello")



window.geometry("300x200")
window.configure(bg="yellow")

label1 = tkinter.Label(
    window,
    text="Hello tkinter!",
    bg="white",
    fg="orange"
)

label1.pack(
    ipadx=10,
    ipady=10,
    fill="both",
    side="bottom"
)

window.mainloop()