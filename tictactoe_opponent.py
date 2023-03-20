import random

class DefaultOpponent:
    def __init__(self, symbol):
        self.symbol = symbol
        self.opponent_symbol = 'O' if symbol == 'X' else 'X'

    def get_symbol(self):
        return self.symbol

    def get_move(self, board):
        # Check for winning move
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = self.symbol
                    if self._check_winner(board, self.symbol):
                        board[row][col] = ' '
                        return row, col
                    else:
                        board[row][col] = ' '

        # Check for blocking move
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = self.opponent_symbol
                    if self._check_winner(board, self.opponent_symbol):
                        board[row][col] = ' '
                        return row, col
                    else:
                        board[row][col] = ' '

        # Choose random move
        empty_spaces = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    empty_spaces.append((row, col))
        if empty_spaces:
            return random.choice(empty_spaces)

    def _check_winner(self, board, symbol):
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
