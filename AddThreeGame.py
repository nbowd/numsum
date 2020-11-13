# Name: Nicholas Bowden
# Date: 11/12/2020
# Description: A two player game where the goal is to select exactly three numbers from a list that sum up to 15. The
# list goes from 1 to 9, and each number can only be selected once per game. The game is a draw if neither plan can make
# a sum of 15 with 3 of the numbers.

class AddThreeGame:
    """Represents Add Three Game. Keeps track of player's score and turns, checks if moves are legal, checks current
    state, and checks for 3 integer sums of 15"""
    def __init__(self):
        """Initializes game settings. Creates moves dictionary, sets current state, and sets current turn to first."""
        self._moves = {
            'first': [],
            'second': [],
            'choices': list(range(1, 10))
        }
        self._current_state = "UNFINISHED"
        self._current_turn = 'first'

    def get_current_state(self):
        """Returns current state of the game"""
        return self._current_state

    def check_sums(self, player):
        """Generates all possible sum combinations and checks if any 3 equal 15."""
        for i in range(0, len(self._moves[player]) - 2):
            for j in range(i + 1, len(self._moves[player]) - 1):
                for k in range(j + 1, len(self._moves[player])):
                    if self._moves[player][i] + self._moves[player][j] + self._moves[player][k] == 15:
                        self._current_state = player.upper() + "_WON"
                        break

    def turn_change(self, player):
        """Changes turn to opposite of current turn."""
        if player == 'first':
            self._current_turn = 'second'
        elif player == 'second':
            self._current_turn = 'first'

    def make_move(self, player, move):
        """Checks if game is unfinished, if move is available and in the correct range, and if all the moves have been
        used. If those pass then the move is recorded to the player that chose it and removed from remaining choices."""
        if self._current_state == "UNFINISHED":
            if player == self._current_turn:  # If correct players turn
                if move in self._moves['choices'] and move in range(1, 10):  # Move is available (on the list, in range)
                    self._moves[player].append(move)
                    self._moves['choices'].remove(move)  # Choice has been removed from list
                else:  # Move is not available
                    return False
                self.check_sums(player)
                if len(self._moves['choices']) == 0:  # Checks if the choice list is empty
                    self._current_state = "DRAW"
                self.turn_change(player)
                return True
            else:  # incorrect players turn
                return False
        else:  # Game is finished
            return False