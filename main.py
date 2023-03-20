import run
from tictactoe.player import *

p1 = DefaultOpponent()
p2 = DefaultOpponent()

p1.set_opponent_symbol('O')
p2.set_opponent_symbol('X')

run.eval_players(p1, p2, 100)