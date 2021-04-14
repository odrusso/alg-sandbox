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


if __name__ == "__main__":
    print(grid_traveler_easy(25, 25))  # should be 6
    print(grid_traveler_manual(25, 25))  # should be 6
