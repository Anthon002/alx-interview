#!/usr/bin/python3
"""Currency exchange module.
"""

def exchangeCurrency(denominations, amount):
    """Determines the fewest number of currency units needed to meet a given
    amount when given a collection of different denomination values.
    """
    if amount <= 0:
        return 0
    remaining = amount
    units_count = 0
    denom_idx = 0
    sorted_denominations = sorted(denominations, reverse=True)
    num_denoms = len(denominations)
    while remaining > 0:
        if denom_idx >= num_denoms:
            return -1
        if remaining - sorted_denominations[denom_idx] >= 0:
            remaining -= sorted_denominations[denom_idx]
            units_count += 1
        else:
            denom_idx += 1
    return units_count
