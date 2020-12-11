from tkinter import *
from math import floor

HEIGHT = 700
WIDTH = 800
root = Tk()

# This is where the text and other game stats will be displayed
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# A separate container inside the canvas to place the buttons
frame = Frame(root, bg='#80c1ff')
frame.place(relx=0.2, relwidth=0.6, relheight=0.6)  # 60% of the screen size

# Expands rows and columns of the frame's grid for widget resizing, without this the buttons stay small.
Grid.rowconfigure(frame, [0, 1, 2], weight=1)
Grid.columnconfigure(frame, [0, 1, 2], weight=1)


def button_click(index, n):
    # Disable the button by index
    buttons[index].config(state="disabled")
    return n

# A collection (list) to hold the references to the buttons created below
buttons = []

for index in range(1, 10):
    n = index
    gr = index - 1
    button = Button(frame, bg="White", text=n, relief=GROOVE,
                    command=lambda index=index - 1, n=n: button_click(index, n))

    # Add the button to the window
    button.grid(row=floor((gr / 3)), column=(gr % 3), sticky="nsew")

    # Add a reference to the button to 'buttons'
    buttons.append(button)
    print(gr)
root.mainloop()
