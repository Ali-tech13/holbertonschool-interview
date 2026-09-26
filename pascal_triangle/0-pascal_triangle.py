#!/usr/bin/python3
"""Module that generates Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's Triangle."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            previous = triangle[i - 1]

            for j in range(len(previous) - 1):
                row.append(previous[j] + previous[j + 1])

            row.append(1)

        triangle.append(row)

    return triangle
