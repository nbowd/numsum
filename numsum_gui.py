from tkinter import *
import tkinter.font as font
from tkmacosx import Button
from math import floor
from AddThreeGame import AddThreeGame


HEIGHT = 700
WIDTH = 800
game = AddThreeGame()
text_color = '#57D9A3'
button_color = '#3B3B3B'
background_color = '#222222'

root = Tk()
root.title("Numsum")
root.resizable(width=False, height=False)

myFont = font.Font(size=30)

# This is where the text and other game stats will be displayed
canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg=background_color)
canvas.pack()

# A separate container inside the canvas to place the buttons
frame = Frame(root)
frame.place(relx=0.2, rely=0.192, relwidth=0.6, relheight=0.6)  # 60% of the screen size

# Expands rows and columns of the frame's grid for widget resizing, without this the buttons stay small.
Grid.rowconfigure(frame, [0, 1, 2], weight=1)
Grid.columnconfigure(frame, [0, 1, 2], weight=1)

player_one_label = Label(canvas, text='Player\n 1', font=['Silom', 40], bg=background_color, fg=text_color)  # Player 1 label
player_one_label.place(relx=0.01, rely=0.02)

player_two_label = Label(canvas, text='Player\n 2', font=['Silom', 40], bg=background_color, fg=text_color)  # Player 2 label
player_two_label.place(relx=0.80, rely=0.02)

canvas.create_line(0, 131, 800, 131, width=5, fill=text_color)  # Line that separates number pad from player labels

def button_click(index, button_number):
    # Disable the button by index
    buttons[index].config(state="disabled", bg=background_color)
    print(button_number)
    game.make_move(button_number)
    print(game.get_current_turn())
    check_game_end()

def check_game_end():
    if game.get_current_state() != 'UNFINISHED':  # Game has a winner or is a draw
        root.title(game.get_current_state())  # Displays in title bar
        for x in range(len(buttons)):  # Disables the remaining buttons
            buttons[x].config(state="disabled", bg=background_color)
        if game.get_current_state() == 'FIRST PLAYER WON!!!':  # Game has a winner, Display WINNER! with astrisk on left or right.
            win_label = Label(canvas, text='*WINNER', font=['Silom', 80], bg=background_color, fg=text_color,
                               justify='center')
            win_label.place(relx=0.23, rely=0.02)
            check_replay()
        elif game.get_current_state() == 'SECOND PLAYER WON!!!':  # Game has a winner, Display WINNER! with astrisk on left or right.
            win_label = Label(canvas, text='WINNER*', font=['Silom', 80], bg=background_color, fg=text_color,
                               justify='center')
            win_label.place(relx=0.28, rely=0.02)
        elif game.get_current_state() == 'DRAW!':  # Game was a draw, display DRAW! in text
            draw_label = Label(canvas, text='DRAW!', font=['Silom', 80], bg=background_color, fg=text_color, justify='center')
            draw_label.place(relx=0.32, rely=0.02)

def check_replay():
    play_again_label = Label(canvas, text='Play Again?', font=['Silom',20], bg=background_color, fg=text_color, justify='center')
    play_again_label.place(relx=0.418,rely=0.8)
    yes_button = Button(canvas, bg=button_color, fg=text_color, text='Yes', width=80, height=60)
    no_button = Button(canvas, bg=button_color, fg=text_color, text='No', width=80, height=60)
    yes_button.place(relx=.395, rely=0.85)
    no_button.place(relx=0.5, rely=0.85)


# A collection (list) to hold the references to the buttons created below
buttons = []

for index in range(1, 10):
    button_number = index
    gr = index - 1
    #  The index-1 accounts for the diff between the buttons numbers starting at 1 and the list indices starting at 0.
    button = Button(frame, bg=button_color, fg=text_color, text=button_number, command=lambda index=index - 1, button_number=button_number: button_click(index, button_number))
    button['font'] = myFont
    # Add the button to the window
    button.grid(row=floor((gr / 3)), column=(gr % 3), sticky="nsew")
    # Add a reference to the button to 'buttons'
    buttons.append(button)


if game.get_current_state() == 'UNFINISHED':
    print(game.get_current_turn())
    print(font.families())

root.mainloop()
