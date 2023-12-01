# easy21
This repository contains my solutions for the [easy 21 assignment](https://www.davidsilver.uk/wp-content/uploads/2020/03/Easy21-Johannes.pdf) from the Reinforcement Learning course held by David Silver at UCL in 2015. <br><br>
The assignment involves the implementation of the following algorithms for a blackjack-like game: _Monte Carlo Control_, _TD Learning_ (Sarsa $\lambda$), and _Linear Function Approximation_. 

### Brief description of the game:
- An infinite deck of black and red cards is used, each with values ranging from 1 to 10.
- Black cards have a positive value, and red cards have a negative value.
- Both the player and the dealer start with a black card.
- The available actions in the game are HIT (take another card) and STICK (let the other player act).
- If either the player or the dealer's sum goes below 1 or above 21, they lose the game.
- The player starts first, and when they STICK, the dealer starts taking turns.
- The dealer's strategy is to HIT until their sum is over 17, at which point they STICK (or lose if their sum exceeds 21).

### Implementation
You can find more implementation details in the associated notebook for each algorithm (e.g. [monte_carlo.ipynb](monte_carlo.ipynb)).
