from enum import Enum
import random
from itertools import product
import numpy as np


class Action(Enum):
    HIT = 0
    STICK = 1


class CardColor(Enum):
    BLACK = 0
    RED = 1


class NewCard:
    def __init__(self, firstCard=False):
        self.number = random.randint(1, 10)
        self.color = CardColor.BLACK if firstCard else self.get_random_color()

    def get_random_color(self):
        colors = [CardColor.BLACK, CardColor.RED]
        return random.choices(colors, weights=[2 / 3, 1 / 3])[0]

    def __str__(self):
        return f"{self.color.name.capitalize()} {self.number}"

    def get_value(self):
        return self.number if self.color == CardColor.BLACK else -self.number


class Env:
    # returns a tuple of the form (dealer_sum, player_sum, reward, terminated)
    def step(self, dealer_card: int, player_sum: int, action: Action):
        if action == Action.HIT.value:
            reward = 0
            player_sum += NewCard().get_value()
            if player_sum > 21 or player_sum < 1:
                reward = -1
            return (dealer_card, player_sum, reward, reward == -1)

        dealer_sum = dealer_card
        while dealer_sum < 17 and dealer_sum > 0:
            dealer_sum += NewCard().get_value()

        if dealer_sum > 21 or dealer_sum < 1:
            return (dealer_sum, player_sum, 1, True)

        reward = 0
        if dealer_sum > player_sum:
            reward = -1
        elif dealer_sum < player_sum:
            reward = 1

        return (dealer_sum, player_sum, reward, True)


def initializeQ():
    possible_states_dealer = np.arange(1, 11)
    possible_states_player = np.arange(1, 22)
    possible_states = list(product(possible_states_dealer, possible_states_player))

    Q = {}
    for state in possible_states:
        Q[state] = {}
        for action in Action:
            Q[state][action.value] = 0
    return Q
