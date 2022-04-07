#!/usr/bin/python3
""" Module for Pascal's triangle """


def pascal_triangle(n):
    """ Returns list of integers representing Pascal's triangle of n """

    if n <= 0:
        return []

    """ initialize array """
    pascal = [[] for idx in range(n)]

    for line in range(n):
        for col in range(line+1):
            if(col < line):
                if(col == 0):
                    pascal[line].append(1)
                else:
                    pascal[line].append(pascal[line-1][col] + pascal[line-1][col-1])
            elif(col == line):
                pascal[line].append(1)

    return pascal
