#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []
    res = [[1]]

    for i in range(n - 1):
        tmp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        res.append(row)
    return res
