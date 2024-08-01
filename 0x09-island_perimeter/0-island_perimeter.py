#!/usr/bin/python3
"""Module for Island perimeter computing.
"""


def island_perimeter(grid):
    """ method to compute perimeter of an island without lakes
    """
    islandPerimeter = 0
    if type(grid) != list:
        return 0
    gridLength = len(grid)
    for i, row in enumerate(grid):
        rowLength = len(row)
        for j, section in enumerate(row):
            if section == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == rowLength - 1 or (rowLength > j + 1 and row[j + 1] == 0),
                i == gridLength - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            islandPerimeter += sum(edges)
    return islandPerimeter
