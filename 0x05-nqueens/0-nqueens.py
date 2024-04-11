#!/usr/bin/python3
""" module for the solution of the N queens problem .
"""
import sys as system


results_ = []
n = 0
pos = None


def input_retrieval():
    """module to retrieve the arguments.
    """
    global n
    n = 0
    if len(system.argv) != 2:
        print("Usage: nqueens N")
        system.exit(1)
    try:
        n = int(system.argv[1])
    except Exception:
        print("N must be a number")
        system.exit(1)
    if n < 4:
        print("N must be at least 4")
        system.exit(1)
    return n


def is_attacking(pos0, pos1):
    """module to check if the queens positions are attacking
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Checking for group in the list of results.
    """
    global results_
    for stn in results_:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def solution_construction(row, group):
    """module to construct solutions for the problem.
    """
    global results_
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            results_.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                solution_construction(row + 1, group)
            group.pop(len(group) - 1)


def get_results_():
    """Get the results.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    solution_construction(a, group)


n = input_retrieval()
get_results_()
for solution in results_:
    print(solution)
