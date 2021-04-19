# Implement a dynamic programming grid-traveler from
# https://www.youtube.com/watch?v=oBt53YbR9Kk
from functools import cache


# This does memoization automatically - pretty groovy
@cache
def grid_traveler_easy(n, m):
    # base cases
    if n <= 1 or m <= 1:
        return 1
    return grid_traveler_easy(n - 1, m) + grid_traveler_easy(n, m - 1)


# This does memoization 'manually' - still pretty easy
def grid_traveler_manual(n, m, memo={}):
    if (n, m) in memo:
        return memo[(n, m)]
    if n <= 1 or m <= 1:
        return 1
    memo[(n, m)] = grid_traveler_manual(n - 1, m) + grid_traveler_manual(n, m - 1)
    return memo[(n, m)]


# I feel like I didn't -really- understand this properly.
def grid_traveler_tab(x, y):
    tab = [[0 for _ in range(x + 1)] for _ in range(y + 1)]
    tab[1][1] = 1
    for i in range(y + 1):
        for j in range(x + 1):
            old = tab[i][j]
            if i + 1 <= y:
                tab[i + 1][j] += old
            if j + 1 <= x:
                tab[i][j + 1] += old
            tab[i][j] = old

    # [print(row) for row in tab]
    return tab[y][x]

if __name__ == "__main__":
    # print(grid_traveler_easy(25, 25))  # should be 6
    # print(grid_traveler_manual(25, 25))  # should be 6

    print(grid_traveler_tab(3, 3))  # should be 6
    print(grid_traveler_tab(4, 7))  # should be >6
    print(grid_traveler_tab(18, 18))  # should be >>>6
