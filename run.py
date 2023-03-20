from tictactoe import board as ttt
import matplotlib.pyplot as plt
from  tictactoe.player import Player


def eval_players(p1 : Player, p2 : Player, num_battles : int, games_per_battle = 10):
    p1_wins = []
    p2_wins = []
    draws = []
    count = []
    #board = ttt.new_board()

    for i in range(1, num_battles):
        print("New game...")
        p1winTot, p2winTot, drawTot = 0, 0, 0
        for j in range(games_per_battle):
            board = ttt.new_board()
            p1win, p2win, draw = ttt.play_game(board, p1, p2)
            p1winTot += p1win
            p2winTot += p2win
            drawTot += draw
        p1_wins.append(p1winTot*100/10)
        p2_wins.append(p2winTot*100/10)
        draws.append(drawTot*100/10)
        count.append(i)

    plt.ylabel('Game outcomes in %')
    plt.xlabel('Game number')

    plt.plot(count, draws, 'r-', label='Draw')
    plt.plot(count, p1_wins, 'g-', label='Player 1 wins')
    plt.plot(count, p2_wins, 'b-', label='Player 2 wins')
    plt.legend(loc='best', shadow=True, fancybox=True, framealpha =0.7)
    plt.show()

# def eval_players2(p1 : Player, p2 : Player, num_battles : int, games_per_battle = 100, loc='best'):
#     p1_wins = []
#     p2_wins = []
#     draws = []
#     count = []
#
#     for i in range(num_battles):
#         p1win, p2win, draw = battle(p1, p2, games_per_battle, True)
#         p1_wins.append(p1win*100.0/games_per_battle)
#         p2_wins.append(p2win*100.0/games_per_battle)
#         draws.append(draw*100.0/games_per_battle)
#         count.append(i*games_per_battle)
#         p1_wins.append(p1win*100.0/games_per_battle)
#         p2_wins.append(p2win*100.0/games_per_battle)
#         draws.append(draw*100.0/games_per_battle)
#         count.append((i+1)*games_per_battle)