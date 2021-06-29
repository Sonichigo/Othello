import copy
from itertools import cycle
import os
from random import shuffle
import sys
import time


BLACK=" ⚫️ "
WHITE=" ⚪️ "
EMPTY="    "
BACK_GREEN = "\x1b[0;30;42m"  # style=0=normal, front=30=black, back=42=green
RESET_COLOR = "\x1b[0m"
DANGEROUS_POSITIONS = [
    (0, 1), (0, 6),
    (1, 0), (1, 1), (1, 6), (1, 7),
    (6, 0), (6, 1), (6, 6), (6, 7),
    (7, 1), (7, 6)
]
CORNER_POSITIONS = [(0, 0), (7, 0), (7, 7), (0, 7)]


class Board():
    def __init__(self):
        self.board = [[EMPTY for i in range(8)] for i in range(8)]
        self.board[3][4] = WHITE
        self.board[3][3] = BLACK
        self.board[4][3] = WHITE
        self.board[4][4] = BLACK

    def __str__(self):
        b = self.board
        return f"""     1    2    3    4    5    6    7    8
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
 A {BACK_GREEN}│{b[0][0]}│{b[0][1]}│{b[0][2]}│{b[0][3]}│{b[0][4]}│{b[0][5]}│{b[0][6]}│{b[0][7]}│{RESET_COLOR} A
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
 B {BACK_GREEN}│{b[1][0]}│{b[1][1]}│{b[1][2]}│{b[1][3]}│{b[1][4]}│{b[1][5]}│{b[1][6]}│{b[1][7]}│{RESET_COLOR} B
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
 C {BACK_GREEN}│{b[2][0]}│{b[2][1]}│{b[2][2]}│{b[2][3]}│{b[2][4]}│{b[2][5]}│{b[2][6]}│{b[2][7]}│{RESET_COLOR} C
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
 D {BACK_GREEN}│{b[3][0]}│{b[3][1]}│{b[3][2]}│{b[3][3]}│{b[3][4]}│{b[3][5]}│{b[3][6]}│{b[3][7]}│{RESET_COLOR} D
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
 E {BACK_GREEN}│{b[4][0]}│{b[4][1]}│{b[4][2]}│{b[4][3]}│{b[4][4]}│{b[4][5]}│{b[4][6]}│{b[4][7]}│{RESET_COLOR} E
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
 F {BACK_GREEN}│{b[5][0]}│{b[5][1]}│{b[5][2]}│{b[5][3]}│{b[5][4]}│{b[5][5]}│{b[5][6]}│{b[5][7]}│{RESET_COLOR} F
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
 G {BACK_GREEN}│{b[6][0]}│{b[6][1]}│{b[6][2]}│{b[6][3]}│{b[6][4]}│{b[6][5]}│{b[6][6]}│{b[6][7]}│{RESET_COLOR} G
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
 H {BACK_GREEN}│{b[7][0]}│{b[7][1]}│{b[7][2]}│{b[7][3]}│{b[7][4]}│{b[7][5]}│{b[7][6]}│{b[7][7]}│{RESET_COLOR} H
   {BACK_GREEN}┼────┼────┼────┼────┼────┼────┼────┼────┼{RESET_COLOR}
     1    2    3    4    5    6    7    8"""

    def has_dominated(self, player):
        """
        Returns False if the other player is still on the board
        """
        for y in range(8):
           for x in range(8):
               if self.board[x][y] != EMPTY and self.board[x][y] != player.color:
                   return False
        return True

    def is_full(self):
        """
        Returns True/False if the board is/isn't full.
        """
        for y in range(8):
           for x in range(8):
               if self.board[x][y] == EMPTY:
                   return False
        return True

    def has_valid_moves(self, player):
        try:
            return True if self._get_valid_moves(player) else False
        except Exception as e:
            return False

    def _get_valid_moves(self, player):
        valid_moves = []
        for y in range(8):
            for x in range(8):
                move = x, y
                if self.is_valid_move(player, move):
                    valid_moves.append(move)
        return valid_moves
      
      
if __name__ == '__main__':
    game = Game()
    game.start()
