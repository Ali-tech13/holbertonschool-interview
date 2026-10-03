#!/usr/bin/python3
"""Determine whether all locked boxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, otherwise False."""
    if not boxes:
        return True

    unlocked = {0}
    keys = [0]

    while keys:
        box = keys.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == len(boxes)
