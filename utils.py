from env import *


def intializeWithZero():
    possible_states_dealer = np.arange(1, 11)
    possible_states_player = np.arange(1, 22)
    possible_states = list(product(possible_states_dealer, possible_states_player))

    Q = {}
    for state in possible_states:
        Q[state] = {}
        for action in Action:
            Q[state][action.value] = 0
    return Q


# returns an epsilon greedy chosen action given the action-value function
# N_0 is a constant, N_s is the dictionary containing how many times each state has been visited
def epsilon_greedy(Q, N_0, N_s, state):
    action_values = Q[state]
    epsilon = N_0 / (N_0 + N_s.get(state, 0))

    # the second check makes sure the algorithm chooses an action
    # at random when the values are the same (rather than always choosing HIT)
    if epsilon > random.uniform(0, 1) or action_values[0] == action_values[1]:
        return random.choice([action.value for action in Action])

    return max(action_values, key=lambda k: action_values[k])
