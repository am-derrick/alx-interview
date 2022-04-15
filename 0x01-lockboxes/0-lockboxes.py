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
    keys = set()
    boxes_open = []
    index = 0

    while index < length:
        i = index
        boxes_open.append(index)
        keys.update(boxes[index])
        for key in keys:
            if key != 0 and key < size and key not in boxes_open:
                index = key
                break
        if i != index:
            continue
        else:
            break

    for index in range(size):
        if index not in boxes_open and index != 0:
            return False
    return True
