from  tictactoe.player import Player
def new_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for tie
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Tie'

    # No winner yet
    return None

def play_game(board, player1: Player, player2: Player):
    player1.set_symbol('X')
    player2.set_symbol('O')

    turn = True
    result = None
    while result is None:
        print("Playing...")
        if turn:
            player1.move(board)
            result = check_winner(board)
            turn = not turn
        else:
            player2.move(board)
            result = check_winner(board)
            turn = not turn

    if result == 'X':
        # Tell players the results: 0 Lose / 1 Win / 2 Tie
        player1.final_result(board, 1)
        player2.final_result(board, 0)
        # Return info: p1 won
        output = (1, 0, 0)
    elif result == 'O':
        # Tell players the results: 0 Lose / 1 Win / 2 Tie
        player1.final_result(board, 0)
        player2.final_result(board, 1)
        # Return info: p2 won
        output = (0, 1, 0)
    else:
        # Tell players the results: 0 Lose / 1 Win / 2 Tie
        player1.final_result(board, 2)
        player2.final_result(board, 2)
        # Return info: tie
        output = (0, 0, 1)

    return output
