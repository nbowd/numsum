# Name: Nicholas Bowden
# Date: 11/12/2020
# Description: A two player game where the goal is to select exactly three numbers from a list that sum up to 15. The
# list goes from 1 to 9, and each number can only be selected once per game. The game is a draw if neither plan can make
# a sum of 15 with 3 of the numbers.

class Numsum:
    """Represents Add Three Game. Keeps track of player's score and turns, checks current state,
    and checks for 3 integer sums of 15"""
    def __init__(self):
        """Initializes game settings. Creates moves dictionary, sets current state, and sets current turn to first."""
        self._moves = {
            'first': [],
            'second': [],
        }
        self._current_state = "UNFINISHED"
        self._current_turn = 'first'
        self.winning_numbers = []
        self.game_length = 0  # Every selected number increments this value by 1. If it reaches 9, the game is a draw.

        # 1 6 2 8 9 3 7 5 4  sample tie game numbers for testing game states

    def get_current_state(self):
        """Returns current state of the game"""
        return self._current_state

    def get_current_turn(self):
        """Returns current state of the game"""
        return self._current_turn

    def check_sums(self):
        """This function checks for sums of 15 using a three pointer array technique."""
        player = self.get_current_turn()
        for index in range(0, len(self._moves[player])):  # main pointer to be iterated over, starts at 0
            # By iteration over the main pointer, a two pointer technique can be used to check the other two values.
            left = index + 1  # left pointer starts one position to the right of the main pointer and increments
            right = len(self._moves[player]) - 1  # right pointer starts at the last position and decrements
            two_sum_goal = 15 - self._moves[player][index]  # sum goal is updated to account for main pointers value.
            while left < right:  # stops when indices overlap
                curr = self._moves[player][left] + self._moves[player][right]
                if curr < two_sum_goal:  # moving left pointer forward one will increase the total of curr
                    left += 1
                elif curr > two_sum_goal:  # moving right pointer back one will decrease total of curr
                    right -= 1
                elif curr == two_sum_goal:  # runs if total sum is 15, index + two sum goal
                    self._current_state = player.upper() + " PLAYER WON!!!"
                    self.winning_numbers.extend(
                        [self._moves[player][index], self._moves[player][left], self._moves[player][right]])
                    #  adds winning numbers to new list to be displayed at the end of a game.
                    break
            # if no matches then no return

    def turn_change(self, player):
        """Changes turn to opposite of current turn."""
        if player == 'first':
            self._current_turn = 'second'
        elif player == 'second':
            self._current_turn = 'first'

    def make_move(self, move):
        """Adds selected move to appropriate players move list, sorts the list and sends it to check_sums to be checked,
        checks if all the moves have been selected, changes turn at the end."""
        if self._current_state == "UNFINISHED":
            player = self.get_current_turn()
            self._moves[player].append(move)
            self._moves[player].sort()  # sorts the lists for the three point array check
            self.check_sums()  # ends loop and game here if player reaches sum of 15
            self.game_length = len(self._moves['first']) + len(self._moves['second'])
            if self.game_length == 9:  # Checks if all the numbers have been chosen.
                self._current_state = "DRAW!"
            self.turn_change(player)
            return True
        else:  # Game is finished
            return False
