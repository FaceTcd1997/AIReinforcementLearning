from tictactoe_board import *
from tictactoe_opponent import *
import random
def get_move_from_input(move):
    match move:
        case 1:
            return 0, 0
        case 2:
            return 0, 1
        case 3:
            return 0, 2
        case 4:
            return 1, 0
        case 5:
            return 1, 1
        case 6:
            return 1, 2
        case 7:
            return 2, 0
        case 8:
            return 2, 1
        case 9:
            return 2, 2
        case _:
            return 0  # 0 is the default case if x is not found

symbols = ['X','O']
board = TicTacToe()
opponent = DefaultOpponent(random.choice(symbols))

winner = None
board.print_board()
print('\n')
while winner is None:
    if opponent.get_symbol() == 'X':
        x_row, x_col = opponent.get_move(board.get_board())

        board.make_move(x_row, x_col)

        winner = board.check_winner()
        if winner is not None:
            break

        board.print_board()

        input_move = int(input("Decide your next move [1->9]: "))
        o_row, o_col = get_move_from_input(input_move)

        board.make_move(o_row, o_col)
        board.print_board()
        print('\n')
    else:
        input_move = int(input("Decide your next move [1->9]: "))
        o_row, o_col = get_move_from_input(input_move)

        board.make_move(o_row, o_col)
        board.print_board()

        winner = board.check_winner()
        if winner is not None:
            break

        x_row, x_col = opponent.get_move(board.get_board())

        board.make_move(x_row, x_col)
        board.print_board()
        print('\n')
    winner = board.check_winner()

print("Ending condition:", winner)