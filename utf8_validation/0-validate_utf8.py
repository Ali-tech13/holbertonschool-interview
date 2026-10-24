
#!/usr/bin/python3
"""Module for UTF-8 validation."""


def validUTF8(data):
    """Check if a list of integers represents valid UTF-8."""
    remaining = 0

    for number in data:
        byte = number & 255

        if remaining == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 6:
                remaining = 1
            elif byte >> 4 == 14:
                remaining = 2
            elif byte >> 3 == 30:
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 2:
                return False
            remaining -= 1

    return remaining == 0
