#!/usr/bin/python3
"""Solves the N Queens problem"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def solve(queens, row):
    """Place queens row by row using backtracking"""
    if row == N:
        print([[i, queens[i]] for i in range(N)])
        return
    for col in range(N):
        if all(col != queens[r] and
               abs(col - queens[r]) != row - r
               for r in range(row)):
            queens[row] = col
            solve(queens, row + 1)


solve([0] * N, 0)
