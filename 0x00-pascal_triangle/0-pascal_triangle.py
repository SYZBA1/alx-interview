#!/usr/bin/python3
"""Solves the pascal triangle Problem"""


def pascal_triangle(n):
    """Prints pascal triangle based on value of n"""
    triangle = []

    for i in range(n):
        hold = []

        if i == 0:
            hold = [1]
            triangle.append(hold)
        elif i == 1:
            hold = [1, 1]
            triangle.append(hold)
        else:
            hold = [1]
            last_value = triangle[len(triangle) - 1]
            for j in range(len(last_value) - 1):
                hold.append(last_value[j] + last_value[j+1])
            hold.append(1)
            triangle.append(hold)

    return triangle
