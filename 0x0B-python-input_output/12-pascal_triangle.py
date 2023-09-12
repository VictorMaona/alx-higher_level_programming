#!/usr/bin/python3
"""the Pascal Triangle function is defined."""


def pascal_triangle(n):
    """Symbolize a Pascal Triangle of size n.

    the triangle is represented by a list of lists of integers.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
