import matplotlib.pyplot as plt
from tictactoe import play_game as play_tictactoe
from connect4_small import play_game as play_connect4

def eval_players_tictactoe(p1, p2, num_battles : int, games_per_battle = 100):
    p1_wins = []
    p2_wins = []
    draws = []
    count = []

    print("Playing...")
    for i in range(1, num_battles):
        p1winTot, p2winTot, drawTot = 0, 0, 0
        for j in range(games_per_battle):
            p1win, p2win, draw = play_tictactoe(p1, p2)
            p1winTot += p1win
            p2winTot += p2win
            drawTot += draw
        p1_wins.append(p1winTot*100/games_per_battle)
        p2_wins.append(p2winTot*100/games_per_battle)
        draws.append(drawTot*100/games_per_battle)
        count.append(i*games_per_battle)
        p1_wins.append(p1winTot*100/games_per_battle)
        p2_wins.append(p2winTot*100/games_per_battle)
        draws.append(drawTot*100/games_per_battle)
        count.append((i+1)*games_per_battle)
    print("End")

    plt.ylabel('Game outcomes in %')
    plt.xlabel('Game number')

    p1_name = p1.get_name()
    p2_name = p2.get_name()

    plt.plot(count, draws, 'r-', label='Tie')
    plt.plot(count, p1_wins, 'g-', label=p1_name)
    plt.plot(count, p2_wins, 'b-', label=p2_name)
    plt.legend(loc='best', shadow=True, fancybox=True, framealpha =0.7)
    plt.show()

    print(p1_name + " number of states explored: " + str(p1.count))
    print(p2_name + " number of states explored: " + str(p2.count))

def eval_players_connect4(p1, p2, num_battles : int, games_per_battle = 100):
    p1_wins = []
    p2_wins = []
    draws = []
    count = []

    print("Playing...")
    for i in range(1, num_battles):
        p1winTot, p2winTot, drawTot = 0, 0, 0
        for j in range(games_per_battle):
            p1win, p2win, draw = play_connect4(p1, p2)
            p1winTot += p1win
            p2winTot += p2win
            drawTot += draw
        if i == 40:
            print()
        p1_wins.append(p1winTot*100/games_per_battle)
        p2_wins.append(p2winTot*100/games_per_battle)
        draws.append(drawTot*100/games_per_battle)
        count.append(i*games_per_battle)
        p1_wins.append(p1winTot*100/games_per_battle)
        p2_wins.append(p2winTot*100/games_per_battle)
        draws.append(drawTot*100/games_per_battle)
        count.append((i+1)*games_per_battle)

    print("End")

    plt.ylabel('Game outcomes in %')
    plt.xlabel('Game number')

    p1_name = p1.get_name()
    p2_name = p2.get_name()

    plt.plot(count, draws, 'r-', label='Tie')
    plt.plot(count, p1_wins, 'g-', label=p1_name)
    plt.plot(count, p2_wins, 'b-', label=p2_name)
    plt.legend(loc='best', shadow=True, fancybox=True, framealpha =0.7)
    plt.show()

    print(p1_name + " number of states explored: " + str(p1.count))
    print(p2_name + " number of states explored: " + str(p2.count))