#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
"""Returns a list of integers representing pascal's triangle of n"""
if n <= 0:
return []

pascal = [[] for i in range(n)]

for li in range(n):
for col in range(li+1):
if
