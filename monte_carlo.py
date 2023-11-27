from itertools import product
from env import *
import random
import numpy as np

possible_states_dealer = np.arange(1, 11)
possible_states_player = np.arange(1, 22)
possible_states = list(product(possible_states_dealer, possible_states_player))


def initializeQ():
    Q = {}
    for state in possible_states:
        Q[state] = {}
        for action in Action:
            Q[state][action.value] = 0
    return Q


# returns an action chosen by "epsilon greedy" given the action-value function
# N_0 is a constant, N_s is the dictionary containing
# how many times each state has been visited
def epsilon_greedy(Q, N_0, N_s, state):
    action_values = Q[state]
    epsilon = N_0 / (N_0 + N_s.get(state, 0))

    # the second check makes sure the algorithm chooses an action
    # at random when the values are the same (rather than always choosing HIT)
    if epsilon > random.uniform(0, 1) or action_values[0] == action_values[1]:
        return random.choice([action.value for action in Action])

    return max(action_values, key=lambda k: action_values[k])


# returns the action-value function found by MC
def monte_carlo_control(env: Env, num_episodes=100, N_0=100):
    # the action-value function, a dictionary with the entries as state: {action, value}
    Q = initializeQ()
    # the number of times each state is visited
    N_s = {}
    # the number of times each (state, action) pair is visited
    N_sa = {}
    wins = 0

    for i in range(num_episodes):
        # generate episode with epsilon-greedy policy
        dealer_sum = NewCard(firstCard=True).get_value()
        player_sum = NewCard(firstCard=True).get_value()
        terminated = False
        episode = []
        G_t = 0
        while not terminated:
            state = (dealer_sum, player_sum)
            N_s[state] = N_s.get(state, 0) + 1
            action = epsilon_greedy(Q, N_0, N_s, state)
            N_sa[(state, action)] = N_sa.get((state, action), 0) + 1
            episode.append((state, action))
            dealer_sum, player_sum, reward, terminated = env.step(
                dealer_sum, player_sum, action
            )
            G_t += reward

        wins += reward == 1
        if i % 10000 == 0 and i > 0:
            print("Episode: %d, score: %f" % (i, (float(wins) / (i) * 100.0)))

        for state, action in episode:
            alpha = 1 / N_sa[(state, action)]
            Q[state][action] = Q[state][action] + alpha * (G_t - Q[state][action])

    return Q


env = Env()
optimal_Q = monte_carlo_control(env, 100000)
sorted_dict = dict(sorted(optimal_Q.items(), key=lambda x: x[0]))
print(sorted_dict)
