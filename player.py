from abc import ABC, abstractmethod
import random
import math

class Player(ABC):
    def __init__(self, symbol, game):
        self.symbol = symbol
        if game == 'ttt':
            self.actions = [i for i in range(0, 9)]
        elif game == 'c4':
            self.actions = [i for i in range(0, 6)]

    def get_name(self):
        return self.__class__.__name__

    def get_symbol(self):
        return self.symbol

    @abstractmethod
    def get_move(self, board):
        pass

    @abstractmethod
    def update(self, result):
        pass

class DefaultOpponent(Player):

    def __init__(self, symbol, game):
        super().__init__(symbol, game)
        self.count = 0

    def get_move(self, board):
        opponent_symbol = 'O' if self.symbol == 'X' else 'X'

        possible_moves = board.get_available_moves()

        # Check winning move
        for move in possible_moves:
            self.count += 1
            index = board.make_move(move, self.symbol)
            if board.check_winner() == self.symbol:
                board.undo_move(index)
                return move
            else:
                board.undo_move(index)

        # Check opponent winning move to block
        for move in possible_moves:
            self.count += 1
            index = board.make_move(move, opponent_symbol)
            if board.check_winner() == opponent_symbol:
                board.undo_move(index)
                return move
            else:
                board.undo_move(index)

        # Random move
        return random.choice(possible_moves)

    def update(self, result):   # Used by QPlayer
        pass

class DefaultOpponentFullRandom(Player):

    def __init__(self, symbol, game):
        super().__init__(symbol, game)
        self.count = 0

    def get_move(self, board):
        possible_moves = board.get_available_moves()

        # Random move
        return random.choice(possible_moves)

    def update(self, result):   # Used by QPlayer
        pass

class MinMaxPlayer(Player):

    def __init__(self, symbol, game):
        super().__init__(symbol, game)
        self.max_depth = 10
        self.game = game
        self.count = 0

    def get_move(self, board):
        if board.is_first_move():
            move = random.choice(board.get_available_moves())
        else:
            if  self.game == 'ttt':
                move = self.minimax_alpha_beta_max_depth(board, self.symbol, depth=9)['move']
            else:
                move = self.minimax_alpha_beta_max_depth(board, self.symbol, depth=5)['move']
        return move

    def minimax_alpha_beta_max_depth(self, board, player, depth, alpha=-math.inf, beta=math.inf):
        max_player = self.symbol  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # Check for end states
        status = board.check_winner()
        if status is not None or depth == 0:
            if status == other_player:
                return {'move': None, 'score': 100 - depth if other_player == max_player else depth - 100}  # There is a winner
            elif status == 'draw':
                return {'move': None, 'score': 30 - depth}  # Draw
            else:
                return {'move': None, 'score': 0}

        if player == max_player:
            best = {'move': None, 'score': -math.inf}  # Max turn
        else:
            best = {'move': None, 'score': math.inf}  # Min turn

        available_moves = board.get_available_moves()
        if len(available_moves) > 0:
            for move in available_moves:
                index = board.make_move(move, player)
                self.count += 1
                score = self.minimax_alpha_beta_max_depth(board, other_player, depth - 1, alpha, beta)
                board.undo_move(index)

                if score['move'] is None:
                    score['move'] = random.choice(available_moves)
                else:
                    score['move'] = move

                if player == max_player:
                    if score['score'] > best['score']:
                        best = score
                    alpha = max(alpha, best['score'])
                    if beta <= alpha:
                        break  # Beta cutoff
                else:
                    if score['score'] < best['score']:
                        best = score
                    beta = min(beta, best['score'])
                    if beta <= alpha:
                        break  # Alpha cutoff

        return best

    def minimax_alpha_beta(self, board, player, alpha=-math.inf, beta=math.inf):
        max_player = self.symbol  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # Check for end states
        status = board.check_winner()
        if status is not None:
            if status == other_player:
                return {'move': None, 'score': 1 if other_player == max_player else -1} # There is a winner
            else:
                return {'move': None, 'score': 0.5} # Draw

        if player == max_player:
            best = {'move': None, 'score': -math.inf}  # Max turn
        else:
            best = {'move': None, 'score': math.inf}  # Min turn

        available_moves = board.get_available_moves()
        if len(available_moves) > 0:
            for move in available_moves:
                index = board.make_move(move, player)
                score = self.minimax_alpha_beta(board, other_player, alpha, beta)
                board.undo_move(index)

                score['move'] = move

                if player == max_player:
                    if score['score'] > best['score']:
                        best = score
                    alpha = max(alpha, best['score'])
                    if beta <= alpha:
                        break # Beta cutoff
                else:
                    if score['score'] < best['score']:
                        best = score
                    beta = min(beta, best['score'])
                    if beta <= alpha:
                        break # Alpha cutoff

        return best

    def update(self, result):   # Used by QPlayer
        pass

class QPlayer(Player):

    def __init__(self, symbol, game, alpha, gamma, epsilon=0.1, delta_epsilon = 0.01):
        super().__init__(symbol, game)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.delta_epsilon = delta_epsilon
        self.q_table = {}
        self.previous_states = []
        self.count = 0

    def get_q(self, state):
        # If there is no state yet create it
        if state not in self.q_table:
            self.q_table[state] = dict({(a, 0.) for a in self.actions})  # Q values initialized as 0
        return self.q_table[state]

    def get_move(self, board):
        if board.is_first_move():
            move = random.choice(board.get_available_moves())
        else:
            state = self.get_q(''.join(board.board))
            available_moves = board.get_available_moves()

            if random.uniform(0, 1) < self.epsilon:
                move = random.choice(available_moves)
            else:
                self.count += len(state)
                state = [(key, value) for key, value in state.items() if key in available_moves]
                max_value = max([i[1] for i in state])
                best_move = [i[0] for i in state if i[1] == max_value]

                if len(best_move) > 1:  # If there are multiple optimal moves
                    move = random.choice(best_move)
                else:
                    move = best_move[0]

            self.epsilon = max(self.epsilon - self.delta_epsilon, 0.0)

            self.previous_states.append((''.join(board.board), move))
        return move

    def update(self, result):
        last = True
        previous = None
        for state in reversed(self.previous_states):
            if last:
                self.q_table[state[0]][state[1]] = result
                last = not last
            else:
                self.q_table[state[0]][state[1]] = (1.0 - self.alpha) * self.q_table[state[0]][state[1]] + self.alpha * self.gamma * max(self.q_table[previous].values())
            previous = state[0]

        self.previous_states = []