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
    # Initialize dp array with infinity
    dp = [float('inf')] * (total + 1)
    print(f"db = {dp}")
    # Base case: 0 coins are needed to make the amount 0
    dp[0] = 0

    # Fill dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return result
    return dp[total] if dp[total] != float('inf') else -1
