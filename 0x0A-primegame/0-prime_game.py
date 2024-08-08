#!/usr/bin/python3
"""moudle for the prime agem.
"""


def isWinner(x, nums):
    """method to determin who the winner of a prime game session with `x` number of rounds
    """
    if x < 1 or not nums:
        return None
    A_win_numbers, B_win_numbers = 0, 0
    n = max(nums)
    primeList = [True for _ in range(1, n + 1, 1)]
    primeList[0] = False
    for i, is_prime in enumerate(primeList, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primeList[j - 1] = False
    # filter the number of primeList less than n in nums for each round
    for _, n in zip(range(x), nums):
        primeCounts = len(list(filter(lambda x: x, primeList[0: n])))
        B_win_numbers += primeCounts % 2 == 0
        A_win_numbers += primeCounts % 2 == 1
    if A_win_numbers == B_win_numbers:
        return None
    return 'Maria' if A_win_numbers > B_win_numbers else 'Ben'
