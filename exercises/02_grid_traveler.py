# A traveler on a 2D grid begins on the top-left corner and the goal is to travel to the bottom-right corner where the
# only moves are down and right.

# Brute force version
def grid_traveler(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


# Memoization version
def grid_traveler(m, n, memo={}):
    # Are the arg in the memo
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    elif m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
        return memo[key]


# Further reduce the number of computations as the reverse of the key is the same value
def grid_traveler(m, n, memo={}):
    # Are the arg in the memo
    key = str(m) + ',' + str(n)
    # The reverse of the key is the same value as the key so we can check if the reverse if computer already instead
    key_swapped = str(n) + ',' + str(m)
    if key in memo:
        return memo[key]
    elif key_swapped in memo:
        return memo[key_swapped]
    elif m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
        return memo[key]


# Tabulation version
import numpy as np


def grid_traveler(m, n):
    table = np.zeros((m + 1, n + 1), dtype=int)
    table[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j + 1] += current
            if i + 1 <= m:
                table[i + 1][j] += current
    return table[m][n]

# grid_traveler(3, 2)
# 3
