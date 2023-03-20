from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, symbol=None):
        self.symbol = symbol

    @abstractmethod
    def set_symbol(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def move(self, board):
        pass

    @abstractmethod
    def final_result(self, board, result):
        pass

class DefaultOpponent(Player):

    def __init__(self, symbol=None, opponent_symbol=None):
        super().__init__(symbol)
        self.opponent_symbol = opponent_symbol

    def set_symbol(self, symbol):
        super().set_symbol(symbol)

    def set_opponent_symbol(self, opponent_symbol):
        self.opponent_symbol = opponent_symbol

    def move(self, board):
        # Check for winning move
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = self.symbol
                    if self.check_winner(board, self.symbol):
                        return board
                    else:
                        board[row][col] = ' '

        # Check for blocking move
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = self.opponent_symbol
                    if self.check_winner(board, self.opponent_symbol):
                        return board
                    else:
                        board[row][col] = ' '

        # Choose random move
        empty_spaces = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    empty_spaces.append((row, col))
        if empty_spaces:
            rnd_move = random.choice(empty_spaces)
            board[rnd_move[0]][rnd_move[1]] = self.symbol

        return board

    def check_winner(self, board, symbol):
        # Check rows
        for row in range(3):
            if board[row][0] == symbol and board[row][1] == symbol and board[row][2] == symbol:
                return True

        # Check columns
        for col in range(3):
            if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
                return True

        # Check diagonals
        if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
            return True

        if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
            return True

        return False

    def final_result(self, board, result):
        pass
