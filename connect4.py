class Connect4:
    def __init__(self):
        self.columns = 7
        self.rows = 6
        self.cells = 42
        self.board = self.make_board()

    def make_board(self):
        return ['-' for _ in range(self.cells)]

    def is_first_move(self):
        return not ('X' in self.board or 'O' in self.board)

    def get_available_moves(self):
        available_moves = []
        for i in range(self.columns):
            if self.board[i] == '-':
                available_moves.append(i)
        return available_moves

    def make_move(self, move, symbol):
        for i in range(self.rows - 1, -1, -1):
            index = i * 7 + move
            if self.board[index] == '-':
                self.board[index] = symbol
                return index

    def undo_move(self, index):
        self.board[index] = '-'

    def check_winner(self):
        # Check rows
        for i in range(0, self.cells, self.columns):
            for j in range(i, i + 4):
                if self.board[j] == self.board[j + 1] == self.board[j + 2] == self.board[j + 3] and self.board[j] != '-':
                    return self.board[j]

        # Check columns
        for i in range(self.columns):
            for j in range(0, 3):
                index = i + j * self.columns
                if self.board[index] == self.board[index + 7] == self.board[index + 14] == self.board[index + 21] and self.board[index] != '-':
                    return self.board[index]


        # Check diagonals (top-left to bottom-right)
        for i in range(0, 15, self.columns):
            for j in range(i, i + 4):
                if self.board[j] == self.board[j + 8] == self.board[j + 16] == self.board[j + 24] and self.board[j] != '-':
                    return self.board[j]

        # Check diagonals (top-right to bottom-left)
        for i in range(3, 18, self.columns):
            for j in range(i, i + 4):
                if self.board[j] == self.board[j + 6] == self.board[j + 12] == self.board[j + 18] and self.board[j] != '-':
                    return self.board[j]

        # Check for draw
        if '-' not in self.board:
            return "draw"

        # Game is not finished
        return None


def display_board(board):
    for i in range(6):
        row = '|'.join(board[(i * 7):(i * 7 + 7)])
        print(row)


def play_game(p1, p2):

    board = Connect4()

    # P1 start
    turn = True
    result = board.check_winner()

    while result is None:

        # P1 turn
        if turn:
            # Get_move
            p1_move = p1.get_move(board)
            # Move
            board.make_move(p1_move, p1.get_symbol())

        # P2 turn
        else:
            # Get_move
            p2_move = p2.get_move(board)
            # Move
            board.make_move(p2_move, p2.get_symbol())

        # Opponent turn
        turn = not turn
        result = board.check_winner()

    # Update agents with result
    if result == p1.get_symbol():
        p1.update(1.)
        p2.update(-1.)
        output = (1, 0, 0) # Result is p1 win
    elif result == p2.get_symbol():
        p1.update(-1.)
        p2.update(1.)
        output = (0, 1, 0) # Result is p2 win
    else:
        p1.update(0.5)
        p2.update(0.5)
        output = (0, 0, 1) # Result is draw

    return output