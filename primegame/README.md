# Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers
starting from `1` up to and including `n`, they take turns choosing a
prime number from the set and removing that number and its multiples
from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each
round. Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.

## Task

### 0. Prime Game

Write a function `def isWinner(x, nums):` that determines the winner
of the most rounds of the prime game.

- `x` is the number of rounds.
- `nums` is an array of `n`.
- Return the name of the player that won the most rounds.
- If the winner cannot be determined, return `None`.
- You can assume `n` and `x` will not be larger than `10000`.
- You cannot import any packages in this task.

File: [0-prime_game.py](./0-prime_game.py)
