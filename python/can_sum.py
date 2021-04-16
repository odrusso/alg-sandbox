from functools import cache


# This does memoization automatically - pretty groovy
@cache
def can_sum_easy(target, nums):
    # base cases
    if target == 0:
        return True
    if target < 0:
        return False

    for modifier in nums:
        if can_sum_easy(target - modifier, nums):
            return True

    return False


def can_sum_manual(target, nums, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True
    if target < 0:
        return False

    for modifier in nums:
        if can_sum_manual(target - modifier, nums, memo):
            return True

    memo[target] = False
    return memo[target]


if __name__ == "__main__":
    print(can_sum_easy(2000, (5, 3, 4, 7, 7, 8, 1, 2, 3, 4)))  # true
    print(can_sum_easy(7, (2, 4)))  # true
    print(can_sum_easy(300, (7, 14)))  # true

    print(can_sum_manual(2000, (5, 3, 4, 7, 7, 8, 1, 2, 3, 4)))  # true
    print(can_sum_manual(7, (2, 4)))  # true
    print(can_sum_manual(300, (7, 14)))  # true
