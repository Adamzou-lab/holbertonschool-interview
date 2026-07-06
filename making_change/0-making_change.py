#!/usr/bin/python3
"""
Module that determines the fewest number of coins needed to meet
a given amount total.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet total.

    Args:
        coins (list): list of the values of the coins available.
        total (int): the amount to meet.

    Returns:
        int: fewest number of coins needed to meet total, 0 if total
            is 0 or less, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    fewest = [0] + [float('inf')] * total

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and fewest[amount - coin] + 1 < fewest[amount]:
                fewest[amount] = fewest[amount - coin] + 1

    return fewest[total] if fewest[total] != float('inf') else -1
