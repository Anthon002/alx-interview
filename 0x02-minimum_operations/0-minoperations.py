#!/usr/bin/python3
'''This module implements the minimum operations challenge
'''


def minOperations(n):
    '''This will compute the least  no. of operations that is needed for the result
    in n H characters.
    '''
    if not isinstance(n, int):
        return 0
    count_operations = 0
    clip_board = 0
    _finished = 1
    while (_finished < n):
        if clip_board == 0:
            clip_board = _finished
            _finished += clip_board
            count_operations += 2
        elif n - _finished > 0 and (n - _finished) % _finished == 0:
            clip_board = _finished
            _finished += clip_board
            count_operations += 2
        elif clip_board > 0:
            _finished += clip_board
            count_operations += 1
    return count_operations
