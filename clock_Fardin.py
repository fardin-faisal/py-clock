import time
from tkinter import*
root = Tk()
root.configure(background = "White")
def start():
    text = time.strftime("%H-%M-%S")
    Label.config(text = text)
    Label.after(200,start)
Label = Label(root,font = ("Bangla",100), fg = "black", bg = "green")
Label.grid(row = 0, column = 1)
print("Done")
start()
root.mainloop()
