import tkinter as ttk

window = ttk.Tk()

colors = ["white", "yellow", "orange", "red", "purple", "black"]
num = 1
size = 100

def updateWindow():
    global num
    global size
    window.geometry(str(size)+"x"+str(size))
    window.configure(bg=colors[num])
    if (6-num) > 1:
        window.after(2000, updateWindow)
    else:
        window.after(2000, explode)
    print(6-num)
    num += 1
    size += 50

def explode():
    print("BOOM!")
    window.destroy()


window.title("My first window")
window.geometry("50x50")
window.configure(bg="white")

window.after(2000, updateWindow)

window.mainloop()