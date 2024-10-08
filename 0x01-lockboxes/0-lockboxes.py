#!/usr/bin/python3
'''
Solution of 0-lockboxes.py
'''


def canUnlockAll(boxes):
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    unlocked = set([0])
    keys = boxes[0]

    while keys:
        new_key = keys.pop()
        if new_key not in unlocked:
            unlocked.add(new_key)
            keys.extend(boxes[new_key])

    return len(unlocked) == len(boxes)
