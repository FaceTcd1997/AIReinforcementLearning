import collections
import numpy as np
import pickle
import os

class Qagent:

    def __init__(self, alpha, gamma):
        self.alpha = alpha
        self.gamma = gamma

        self.actions = []
        for row in range(3):
            for col in range(3):
                self.actions.append((row,col))

        self.Q = {}
        for action in self.actions:
            self.Q[action] = collections.defaultdict(int)

        self.rewards = []

    def get_action(self, state):
        possible_actions = [a for a in self.actions if state[a[0]][a[1]] == ' ']
        values = np.array([self.Q[a][state] for a in possible_actions])

        v_max = np.where(values == np.max(values))[0]
        if len(v_max) > 1:
            action = np.random.choice(v_max, 1)[0]
        else:
            action = v_max[0]
        next_action = possible_actions[action]

        return next_action

    def update(self, prev_state, state, action, reward):
        if state is not None:
            possible_actions = [a for a in self.actions if state[a[0]][a[1]] == ' ']
            Q_options = [self.Q[a][state] for a in possible_actions]

            self.Q[action][state] += self.alpha * (reward + self.gamma * max(Q_options) - self.Q[action][state])
        else:
            self.Q[action][state] += self.alpha * (reward - self.Q[action][state])

        self.rewards.append(reward)



    # def save(self):
    #     path = "../agent/q_agent.pkl"
    #     os.path.normpath(path)
    #
    #     if os.path.isfile(path):
    #         os.remove(path)
    #     f = open(path, 'wb')
    #     pickle.dump(self, f)
    #     f.close()