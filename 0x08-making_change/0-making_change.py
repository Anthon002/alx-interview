#!/usr/bin/python3
"""Currency exchange module.
"""

def makeChange(coins, total):
    """Determines the fewest number of currency units needed to meet a given
    total when given a collection of different denomination values.
    """
    if total <= 0:
        return 0
    remaining = total
    units_count = 0
    denom_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    num_denoms = len(coins)
    while remaining > 0:
        if denom_idx >= num_denoms:
            return -1
        if remaining - sorted_coins[denom_idx] >= 0:
            remaining -= sorted_coins[denom_idx]
            units_count += 1
        else:
            denom_idx += 1
    return units_count
