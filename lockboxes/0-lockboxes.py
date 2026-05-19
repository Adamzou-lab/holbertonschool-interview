#!/usr/bin/python3
"""Module that solves the lockboxes problem using depth-first search"""


def canUnlockAll(boxes):
    """Determines if all locked boxes can be opened"""
    keys = [0]
    opened = set()

    while keys:
        key = keys.pop()
        opened.add(key)

        if key < len(boxes):
            for k in boxes[key]:
                if k not in opened and k < len(boxes):
                    keys.append(k)

    return len(opened) == len(boxes)
