#!/usr/bin/python3
"""
n number of locked boxes, numberred sequnetially form 0 to n-1
and may contain keys to other boxes. Method to determine if all boxes can open
"""


def canUnlockAll(boxes):
    """method to determine if all boxes can open"""
    if not boxes:
        return False
    size = len(boxes)
    check = {}
    index = 0

    for box in boxes:
        if len(box) == 0 or index == 0:
            check[index] = -1
        for key in box:
            if key < size and key != index:
                check[key] = key
        if len(check) == size:
            return True:
        index += 1
    return False
