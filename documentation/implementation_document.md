# Implementation


## General structure

In the RPS_CFR you can find the implementation for rock paper scissors which is a normal form game and Kuhns poker in KUHNS_CFR which is a simplified poker format with 3 card deck and both players get one card.
Ive also implement ArrayMethods class to help with some vector operations.



## Time complexity

The normal form game runs in O(N) and extended form game is O(N(num_of_actions*decision_nodes)) which in Knuhns poker is check/bet and JQ JK QJ QK KJ KQ where nodes are the hand permutation decision nodes and edges actions.

## Improvements and possible features

Implement CFR+ or CFR with chance sampling to improve the speed.


Sources:

http://modelai.gettysburg.edu/2013/cfr/cfr.pdf

http://papers.nips.cc/paper/3306-regret-minimization-in-games-with-incomplete-information.pdf

http://webdocs.cs.ualberta.ca/~duane/publications/pdf/2010aamas.pdf

https://pdfs.semanticscholar.org/7acd/209a8ae26348c5dc96aedd7b58d95fbf49bf.pdf

https://justinsermeno.com/posts/cfr/

https://int8.io/counterfactual-regret-minimization-for-poker-ai/

https://hackernoon.com/artificial-intelligence-poker-and-regret-part-1-36c78d955720
