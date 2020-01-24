## CFR - Counterfactual regret minimization

## What problem does it solve?

Approximates exploitable strategies for one player or nash equilibrium strategy for both players in two player uncomplete information games. Normal form games like rock paper scissors or extended form games like 1 card poker, texas holdem etc.

## What inputs does the program get?

In normal form games we get all possible actions in an array and we iterate over it while the strategy improves. In extended form games Program gets the complete game-tree as input and then we traverse it in depth-first manner while updating the nodes and getting closer to the nash equilibrium approximation.


## Time complexity

It performs a Depht-first traverse n times so it should be O(N*(V+E))

## Sources:
http://modelai.gettysburg.edu/2013/cfr/cfr.pdf
http://cs.gettysburg.edu/~tneller/modelai/2013/cfr/
