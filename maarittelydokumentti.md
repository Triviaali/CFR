## CFR - Counterfactual regret minimization

## What is CFR and what does it do?

Counterfactual Regret Minimisation is a reinforcement learning algorithm for mostly zero-sum two player games altough winning 3 player agents have been developed for poker. It's improved version CFR+ helped solve the game of heads-up (1 on 1) limit Texas hold'em poker [http://poker.srv.ualberta.ca/about]. The algorithm itself is a self playing A.I model. Basically two AI agents playing against each other and learning the game from scratch. In many cases, it's and agent playing against itself, so it learns twice as fast. CFR does not use neural networks to calculate probabilities or the value of a particular move. Instead by playing itself over large amount of hands/rounds it sums up the regret for each action in certain position. The more it plays the closer it gets to optimal strategy namely nash equilibrium. Nash equilibrium is defined as: "Nash Equilibrium is a proposed solution of a non-cooperative game involving two or more players in which each player is assumed to know the equilibrium strategies of the other players, and no player has anything to gain by changing only their own strategy." Read more at [https://en.wikipedia.org/wiki/Nash_equilibrium]


### Regret Matching
Regret matching is an algorithm that seeks to minimise regret about its decisions at each step/move of a game. As the name suggests, it learns from past behaviours to inform future decisions by favouring the action it regretted not having taken previously. In laymans terms it favours action that has resulted in positive outcomes and avoids actions that have resulted in negative outcomes.

## What inputs does the program get?

Depends on the game the agents are being trained on. As an example lets formalize a normal-form, two-player, zero sum game rock paper scissors.
It's a tuple of form < N, A, u>
```
* N = 1,...n of players, in this case N = {1, 2}
* S = finite set of actions, in this case the actions are mirrrored so {R, P, S}
* A = S x ... x Sn = {(R,R,...,(S, P)} each combination is called an action profile.
* u = is a function mapping each action profile to a vector to utilities/payoffs
```
| Rock | Paper | Scissors |          |
|------|-------|----------|----------|
| 0    | -1    | 1        | Rock     |
| 1    | 0     | -1       | Paper    |
| -1   | 1     | 0        | Scissors |


In normal-form games the game rules can be presented as a 1d array or a 2d array as above then we play the agents against each other while updating strategies of both players with regret matching after each round.


## Time complexity

On normal-form games the time complexity is just the number of the iterations.
On extend-form games the whole game tree expressed as nodes is traversed n times so: O(N*(V+E))

## Sources:
http://modelai.gettysburg.edu/2013/cfr/cfr.pdf
http://cs.gettysburg.edu/~tneller/modelai/2013/cfr/
