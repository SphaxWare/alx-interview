#!/usr/bin/python3
"""
0. Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    current = 0
    counter = 0
    for coin in coins:
        while coin <= total:
            current = total // coin
            counter += current
            total -= current * coin
            if total == 0:
                return counter
    return -1
