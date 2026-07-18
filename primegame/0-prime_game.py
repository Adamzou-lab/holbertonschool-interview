#!/usr/bin/python3
"""
Module that determines the winner of the prime game over several rounds.
"""


def isWinner(x, nums):
    """Determine who wins the most rounds of the prime game.

    Args:
        x (int): the number of rounds.
        nums (list): list of n values, one per round.

    Returns:
        str: name of the player that won the most rounds ("Maria" or
            "Ben"), or None if the winner cannot be determined.
    """
    if x <= 0 or not nums:
        return None

    n = max(nums)
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False

    primes_count = [0] * (n + 1)
    for i in range(1, n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for round_n in nums:
        if primes_count[round_n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
