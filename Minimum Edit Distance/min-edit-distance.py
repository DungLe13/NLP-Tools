#!/usr/bin/env python3
"""
    min-edit-distance.py - Levenshtein Minimum Edit Distance
    Author: Dung Le (dungle@bennington.edu)
    Date: 09/23/2017
"""

# Only work if len(source) = len(target)
def minEditDistance(source, target):
    n = len(target)
    m = len(source)
    D = [[0 for x in range(n+1)] for y in range(m+1)]

    # Initialization
    D[0][0] = 0
    for i in range(1, n+1):
        D[i][0] = D[i-1][0] + ins_cost(target[i-1])

    for j in range(1, m+1):
        D[0][j] = D[0][j-1] + del_cost(source[j-1])

    # Recurrence relation
    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = min(D[i][j-1] + del_cost(source[j-1]),
                          D[i-1][j-1] + sub_cost(source[j-1], target[i-1]),
                          D[i-1][j] + ins_cost(target[i-1]))

    return D[n][m]

# Costs for Deletion, Insertion and Substitution
def del_cost(c):
    return 1

def ins_cost(c):
    return 1

def sub_cost(s, t):
    if s == t:
        return 0
    else:
        return 2
