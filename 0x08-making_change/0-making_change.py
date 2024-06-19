#!/usr/bin/python3
"""
Make Change
"""
from typing import List 


def makeChange(coins: List, total: int) -> int:
    """ Main Entrypoint
    """
    minCoins = [float('inf')] * (total + 1)
    minCoins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    return -1 if minCoins[total] == float('inf') else minCoins[total]
