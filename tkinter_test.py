from tkinter import *
#  creates window
root = Tk()

e = Entry(root, width=50)
e.pack()
def my_click():
    labs = Label(root, text= e.get())
    labs.pack()

fer = Button(root, text='Enter your name', command=my_click)

fer.pack()
root.mainloop()


# buttons[index].config(state="disabled")