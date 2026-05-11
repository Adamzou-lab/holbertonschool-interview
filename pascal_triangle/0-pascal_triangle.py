#!/usr/bin/env python3
def pascal_triangle(n):
    triangle = [[1]]
    if n <= 0:
        return []
    for i in range(n - 1):
        prev = triangle[-1]
        new = [1]
        for i in range(len(prev) - 1):
            new.append(prev[i] + prev[i + 1])
        new.append(1)
        triangle.append(new)
    return triangle
