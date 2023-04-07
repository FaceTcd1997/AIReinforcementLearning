from player import *
from run import eval_players_tictactoe, eval_players_connect4

"""DECIDE THE GAME AND THE COMBINATION OF PLAYERS THAT PLAY BY UNCOMMENT THE LINES"""

"""---------------------------TIC TAC TOE----------------------------"""
# PLAYER ONE
#p1 = DefaultOpponentFullRandom(symbol='X', game='ttt')
#p1 = DefaultOpponent(symbol='X', game='ttt')
#p1 = MinMaxPlayer(symbol='X', game='ttt')
#p1 = QPlayer(symbol='X', game='ttt', alpha=0.8, gamma=0.95, epsilon=0.4, delta_epsilon=0.00001)
# PLAYER TWO
#p2 = DefaultOpponentFullRandom(symbol='O', game='ttt')
#p2 = DefaultOpponent(symbol='O', game='ttt')
#p2 = MinMaxPlayer(symbol='O', game='ttt')
#p2 = QPlayer(symbol='O',game='ttt', alpha=0.8, gamma=0.95, epsilon=0.4, delta_epsilon=0.00001)
# TIC TAC TOE SIMULATION
#eval_players_tictactoe(p1, p2, 100)

"""----------------------------CONNECT 4-----------------------------"""
# PLAYER ONE
#p1 = DefaultOpponentFullRandom(symbol='X', game='c4')
#p1 = DefaultOpponent(symbol='X', game='c4')
#p1 = MinMaxPlayer(symbol='X', game='c4')
#p1 = QPlayer(symbol='X', game='c4', alpha=0.8, gamma=0.95, epsilon=0.3, delta_epsilon=0.000005)
# PLAYER TWO
#p2 = DefaultOpponentFullRandom(symbol='O', game='c4')
#p2 = DefaultOpponent(symbol='O', game='c4')
#p2 = MinMaxPlayer(symbol='O', game='c4')
#p2 = QPlayer(symbol='O',game='c4', alpha=0.8, gamma=0.95, epsilon=0.3, delta_epsilon=0.000005)
# CONNECT 4 SIMULATION
#eval_players_connect4(p1, p2, 100)


