#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the
    island described in grid
    """
    p = 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top neighbor
                if i == 0 or grid[i-1][j] == 0:
                    p += 1
                # Check bottom neighbor
                if i == rows-1 or grid[i+1][j] == 0:
                    p += 1
                # Check left neighbor
                if j == 0 or grid[i][j-1] == 0:
                    p += 1
                # Check right neighbor
                if j == cols-1 or grid[i][j+1] == 0:
                    p += 1
    return p
