from tkinter import *
import tkinter.font as font
from tkmacosx import Button
from math import floor
from numsum_game_logic import Numsum
import sys
import os


class GuiNumsum:
    """Contains GUI setup for Numsum game."""
    def __init__(self):
        """Initialize all the variables of the GUI and of Numsum."""
        self.height = 700
        self.width = 800
        self.game = Numsum()
        self.text_color = '#57D9A3'
        self.button_color = '#3B3B3B'
        self.background_color = '#222222'
        self.font = 'Silom'

        self._root = Tk()
        self._root.title("Numsum")
        self._root.resizable(width=False, height=False)  # Fixed size

        # The canvas is where the text and other game stats will be displayed
        self.canvas = Canvas(self._root, height=self.height, width=self.width, bg=self.background_color)
        self.canvas.pack()

        # A separate container inside the canvas to place the button grid
        self.frame = Frame(self._root)
        self.frame.place(relx=0.2, rely=0.192, relwidth=0.6, relheight=0.6)  # 60% of the screen size
        # Expands rows and columns of the frame's grid for widget resizing, without this the buttons stay small.
        Grid.rowconfigure(self.frame, [0, 1, 2], weight=1)
        Grid.columnconfigure(self.frame, [0, 1, 2], weight=1)

        # Player 1 label
        self.player_one_label = Label(self.canvas, text='Player\n 1', font=[self.font, 40],
                                      bg=self.background_color, fg=self.text_color)
        self.player_one_label.place(relx=0.01, rely=0.02)

        # Player 2 label
        self.player_two_label = Label(self.canvas, text='Player\n 2', font=[self.font, 40],
                                      bg=self.background_color, fg=self.text_color)
        self.player_two_label.place(relx=0.80, rely=0.02)

        # A solid line that separates number pad from player labels
        self.canvas.create_line(0, 131, 800, 131, width=5, fill=self.text_color)

        # A collection (list) to hold the references to the buttons created below
        self.buttons = []
        self._button_font_size = font.Font(size=30)  # Buttons don't work consistently on MacOS, this setting helps out.

        # Initializes buttons in frame
        for index in range(1, 10):
            button_number = index
            # index-1 because the buttons numbers start at 1 and the list indices starting at 0.
            grid_index = index - 1
            # lambda passes vars from this function as parameters to button_click and calls that function on each press.
            button = Button(self.frame, bg=self.button_color, fg=self.text_color, text=button_number,
                            command=lambda index=grid_index, button_number=button_number: self.button_click(index,
                                                                                                      button_number))
            # sets font on separate line because of MacOS button issues.
            button['font'] = self._button_font_size
            # Add the button to the window
            button.grid(row=floor((grid_index / 3)), column=(grid_index % 3), sticky="nsew")
            # Add a reference to the newly created button to the list 'buttons'
            self.buttons.append(button)

        # Rules button, triggers popout window
        self.rules_button = Button(self.canvas, text='Rules', font=[self.font, 15], bg=self.button_color,
                                   fg=self.text_color, width=60, height=40, command=self.popup_rules)
        self.rules_button.place(relx=0.91, rely=0.93)

        # Main tkinter loop
        self._root.mainloop()

    def button_click(self, index, button_number):
        """This function runs after each button is selected by a player. It takes the number selected and displays the
        chosen number. It then registers the move with the game, and checks to see if
        that move has ended the game."""
        # Disable the button by index
        self.buttons[index].config(state="disabled", bg=self.background_color)

        self.display_chosen_number(button_number)
        self.game.make_move(button_number)

        self.check_game_end()

    def display_chosen_number(self, display_number):
        """Displays selected number on appropriate players side of the screen in a column."""

        #  Calculates space between displayed numbers by multiplying game length by 0.05, so every move increases the
        #  space by that amount. This function runs BEFORE the move is made so 1 is added to game length preemptively.
        current_game_length = (self.game.game_length + 1) * 0.05
        if self.game.get_current_turn() == 'first':  # add to left side of screen
            screen_number = Label(self.canvas, text=display_number, font=[self.font, 40], bg=self.background_color,
                                  fg=self.text_color)
            screen_number.place(relx=0.085, rely=(0.25+current_game_length))

        else:  # it is second players turn, add to right side of screen
            screen_number = Label(self.canvas, text=display_number, font=[self.font, 40],
                                  bg=self.background_color, fg=self.text_color)
            screen_number.place(relx=0.85, rely=(0.2 + current_game_length))

    def check_game_end(self):
        """Checks if the game has ended, display's winner or draw, the calls the replay game function to see how the
        program should proceed."""
        if self.game.get_current_state() != 'UNFINISHED':  # Game has a winner or is a draw
            self._root.title(self.game.get_current_state())  # Display's game state in title bar

            for x in range(len(self.buttons)):  # Disables the remaining buttons
                self.buttons[x].config(state="disabled", bg=self.background_color)

            self.check_replay()  # Play again buttons appears

            # Game has a winner, Display WINNER! with asterisk on left or right.
            if self.game.get_current_state() == 'FIRST PLAYER WON!!!':
                win_label = Label(self.canvas, text='*WINNER', font=[self.font, 80], bg=self.background_color,
                                  fg=self.text_color, justify='center')
                win_label.place(relx=0.23, rely=0.02)

            # Game has a winner, Display WINNER! with asterisk on left or right.
            elif self.game.get_current_state() == 'SECOND PLAYER WON!!!':
                win_label = Label(self.canvas, text='WINNER*', font=[self.font, 80], bg=self.background_color,
                                  fg=self.text_color, justify='center')
                win_label.place(relx=0.28, rely=0.02)

            # Game was a draw, display DRAW! in text
            elif self.game.get_current_state() == 'DRAW!':
                draw_label = Label(self.canvas, text='DRAW!', font=[self.font, 80], bg=self.background_color,
                                   fg=self.text_color, justify='center')
                draw_label.place(relx=0.32, rely=0.02)

    def restart_program(self):
        """Restarts the current program."""
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def check_replay(self):
        """Displays 'play again' label with 'yes' and 'no' buttons. Selecting 'yes' runs restart_program function,
        selecting 'no' exits the program."""
        play_again_label = Label(self.canvas, text='Play Again?', font=[self.font, 20], bg=self.background_color,
                                 fg=self.text_color, justify='center')
        play_again_label.place(relx=0.418, rely=0.8)

        yes_button = Button(self.canvas, bg=self.button_color, fg=self.text_color, font=[self.font, 15], text='Yes',
                            width=80, height=60, command=self.restart_program)
        no_button = Button(self.canvas, bg=self.button_color, fg=self.text_color, font=[self.font, 15], text='No',
                           width=80, height=60, command=sys.exit)

        yes_button.place(relx=.395, rely=0.85)
        no_button.place(relx=0.5, rely=0.85)

    def popup_rules(self):
        """Creates 'Rules' button in bottom right of screen, click it opens a popup window with the rules and an 'Okay'
        button to close the window and return to the game."""
        # Toplevel instead of Tk for secondary windows, you can only have one instance of Tk which is your main.
        popup = Toplevel(bg=self.background_color)
        popup.wm_title('Rules')
        popup_text = "Welcome to Numsum!\n" \
                     "The goal is to make a sum of 15 using exactly 3 numbers.\n" \
                     "When a number is chosen by one player, it becomes unavailable to choose for the other player.\n" \
                     "If all the numbers are selected and neither player can make a sum of 15, the game is a draw.\n" \
                     "Good Luck!"
        popup_label = Label(popup, text=popup_text, font=[self.font, 15], bg=self.background_color, fg=self.text_color,
                            justify='center')
        popup_label.pack()

        # .destroy will close that window
        confirm_button = Button(popup, text='Okay', bg=self.button_color, fg=self.text_color, font=[self.font, 15],
                                command=popup.destroy)
        confirm_button.pack()
        popup.mainloop()


def main():
    """Main function for when this program is run directly"""
    game = GuiNumsum()


if __name__ == '__main__':
    main()
