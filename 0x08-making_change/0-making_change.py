#!/usr/bin/python3
"""
Make Change
"""
from typing import List


def makeChange(coins: List, total: int) -> int:
    """ Main Entrypoint
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    steps = 0
    coins = reversed(sorted(coins))

    for coin in coins:
        while coin <= total:
            total -= coin
            steps += 1
        if (total == 0):
            return steps
    return -1
