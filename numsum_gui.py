from tkinter import *
import tkinter.font as font
from tkmacosx import Button
from math import floor
from AddThreeGame import AddThreeGame
import sys
import os

class GuiNumsum:
    """!"""
    def __init__(self):
        """!"""
        self.height = 700
        self.width = 800
        self.game = AddThreeGame()
        self.text_color = '#57D9A3'
        self.button_color = '#3B3B3B'
        self.background_color = '#222222'

        self._root = Tk()
        self._root.title("Numsum")
        self._root.resizable(width=False, height=False)

        self._player_font_size = font.Font(size=30)

        # This is where the text and other game stats will be displayed
        self.canvas = Canvas(self._root, height=self.height, width=self.width, bg=self.background_color)
        self.canvas.pack()

        # A separate container inside the canvas to place the buttons
        self.frame = Frame(self._root)
        self.frame.place(relx=0.2, rely=0.192, relwidth=0.6, relheight=0.6)  # 60% of the screen size

        # Expands rows and columns of the frame's grid for widget resizing, without this the buttons stay small.
        Grid.rowconfigure(self.frame, [0, 1, 2], weight=1)
        Grid.columnconfigure(self.frame, [0, 1, 2], weight=1)

        self.player_one_label = Label(self.canvas, text='Player\n 1', font=['Silom', 40],
                                      bg=self.background_color, fg=self.text_color)  # Player 1 label
        self.player_one_label.place(relx=0.01, rely=0.02)

        self.player_two_label = Label(self.canvas, text='Player\n 2', font=['Silom', 40],
                                      bg=self.background_color, fg=self.text_color)  # Player 2 label
        self.player_two_label.place(relx=0.80, rely=0.02)
        # A solid line that separates number pad from player labels
        self.canvas.create_line(0, 131, 800, 131, width=5, fill=self.text_color)
        # A collection (list) to hold the references to the buttons created below
        self.buttons = []
        # Initializes buttons in frame
        for index in range(1, 10):
            button_number = index
            gr = index - 1
            #  The index-1 accounts for the diff between the buttons numbers starting at 1 and the list indices starting at 0.
            button = Button(self.frame, bg=self.button_color, fg=self.text_color, text=button_number,
                            command=lambda index=index - 1, button_number=button_number: self.button_click(index,
                                                                                                      button_number))
            button['font'] = self._player_font_size
            # Add the button to the window
            button.grid(row=floor((gr / 3)), column=(gr % 3), sticky="nsew")
            # Add a reference to the button to 'buttons'
            self.buttons.append(button)
        self._root.mainloop()

    def button_click(self, index, button_number):
        # Disable the button by index
        self.buttons[index].config(state="disabled", bg=self.background_color)
        print(button_number)
        self.display_chosen_number(button_number)
        self.game.make_move(button_number)
        print(self.game.get_current_turn())
        self.check_game_end()

    def display_chosen_number(self, display_number):
        current_game_length = (self.game.game_length + 1) * 0.05
        if self.game.get_current_turn() == 'first':
            screen_number = Label(self.canvas, text=display_number, font=['Silom', 40],
                                      bg=self.background_color, fg=self.text_color)
            screen_number.place(relx=0.085, rely=(0.25+current_game_length))
        else:  # it is second players turn
            screen_number = Label(self.canvas, text=display_number, font=['Silom', 40],
                                  bg=self.background_color, fg=self.text_color)
            screen_number.place(relx=0.85, rely=(0.2 + current_game_length))

    def check_game_end(self):
        if self.game.get_current_state() != 'UNFINISHED':  # Game has a winner or is a draw
            self._root.title(self.game.get_current_state())  # Displays in title bar
            for x in range(len(self.buttons)):  # Disables the remaining buttons
                self.buttons[x].config(state="disabled", bg=self.background_color)
            self.check_replay()  # Play again buttons appears
            if self.game.get_current_state() == 'FIRST PLAYER WON!!!':  # Game has a winner, Display WINNER! with astrisk on left or right.
                win_label = Label(self.canvas, text='*WINNER', font=['Silom', 80], bg=self.background_color, fg=self.text_color,
                                   justify='center')
                win_label.place(relx=0.23, rely=0.02)

            elif self.game.get_current_state() == 'SECOND PLAYER WON!!!':  # Game has a winner, Display WINNER! with astrisk on left or right.
                win_label = Label(self.canvas, text='WINNER*', font=['Silom', 80], bg=self.background_color, fg=self.text_color,
                                   justify='center')
                win_label.place(relx=0.28, rely=0.02)
            elif self.game.get_current_state() == 'DRAW!':  # Game was a draw, display DRAW! in text
                draw_label = Label(self.canvas, text='DRAW!', font=['Silom', 80], bg=self.background_color, fg=self.text_color, justify='center')
                draw_label.place(relx=0.32, rely=0.02)

    def check_replay(self):
        play_again_label = Label(self.canvas, text='Play Again?', font=['Silom',20], bg=self.background_color, fg=self.text_color, justify='center')
        play_again_label.place(relx=0.418,rely=0.8)
        yes_button = Button(self.canvas, bg=self.button_color, fg=self.text_color, text='Yes', width=80, height=60, command=self.restart_program)
        no_button = Button(self.canvas, bg=self.button_color, fg=self.text_color, text='No', width=80, height=60, command=sys.exit)
        yes_button.place(relx=.395, rely=0.85)
        no_button.place(relx=0.5, rely=0.85)

    def restart_program(self):
        """Restarts the current program."""
        python = sys.executable
        os.execl(python, python, *sys.argv)


test = GuiNumsum()
