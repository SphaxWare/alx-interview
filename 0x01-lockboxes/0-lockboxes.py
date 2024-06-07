#!/usr/bin/python3
""" Lockboxes.exe """


def canUnlockAll(boxes):
    """
    Check lockboxes and see if
    if can unlock them all
    """
    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
