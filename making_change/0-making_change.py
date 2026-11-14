#!/usr/bin/python3
"""Find the minimum number of coins needed to make a given amount."""


def makeChange(coins, total):
    """Return the minimum number of coins needed to make total."""
    if total <= 0:
        return 0

    coins = sorted(set(coin for coin in coins if coin <= total))

    if not coins:
        return -1

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    if dp[total] == total + 1:
        return -1

    return dp[total]
