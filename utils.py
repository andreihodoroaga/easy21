from env import *
import json


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


def compute_mean_squared_error(current_Q, optimal_Q):
    mse = 0

    for state in current_Q.keys():
        for action in current_Q[state].keys():
            mse += (optimal_Q[state][action] - current_Q[state][action]) ** 2

    return mse


def get_optimal_Q():
    with open("optimal_Q.json", "r") as json_file:
        optimal_Q_json = json.load(json_file)

    # de-stringify dict keys
    optimal_Q = {}
    for outer_key_str, inner_dict in optimal_Q_json.items():
        outer_key = eval(outer_key_str)
        inner_dict_original_keys = {
            eval(inner_key): value for inner_key, value in inner_dict.items()
        }
        optimal_Q[outer_key] = inner_dict_original_keys

    return optimal_Q
