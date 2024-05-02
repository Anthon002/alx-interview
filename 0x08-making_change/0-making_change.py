#!/usr/bin/python3
"""module for making change
"""


def makeChange(coins, total):
    """ method to Determines the fewest number of coins that is needed to reach a change amount.
    """
    if total <= 0:
        return 0
    rem = total
    count_coin = 0
    idxcoin_ = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if idxcoin_ >= n:
            return -1
        if rem - sorted_coins[idxcoin_] >= 0:
            rem -= sorted_coins[idxcoin_]
            count_coin += 1
        else:
            idxcoin_ += 1
    return count_coin
