class TicTacToe:
    def __init__(self):
        self.cells = 9
        self.board = self.make_board()

    def make_board(self):
        return ['-' for _ in range(self.cells)]

    def is_first_move(self):
        return not ('X' in self.board or 'O' in self.board)

    def get_available_moves(self):
        available_moves = []
        for i in range(len(self.board)):
            if self.board[i] == '-':
                available_moves.append(i)
        return available_moves

    def make_move(self, move, symbol):
        self.board[move] = symbol
        return move

    def undo_move(self, index):
        self.board[index] = '-'

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] and self.board[i] != '-':
                return self.board[i]

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] and self.board[i] != '-':
                return self.board[i]

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != '-':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != '-':
            return self.board[2]

        # Check for draw
        if '-' not in self.board:
            return "draw"

        # Game is not finished
        return None

def play_game(p1, p2):

    board = TicTacToe()

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
