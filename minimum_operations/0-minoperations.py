#!/usr/bin/python3
"""Module for computing minimum Copy All / Paste operations."""


def minOperations(n):
    """Return the fewest operations to get exactly n 'H' characters."""
    if n < 2:
        return 0

    ops = 0
    divisor = 2

    while divisor <= n:
        while n % divisor == 0:
            ops += divisor
            n //= divisor
        divisor += 1

    return ops
