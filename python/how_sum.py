from functools import cache


@cache
def how_sum_easy(target, nums):
    # base cases
    if target == 0:
        return []
    if target < 0:
        return False

    for modifier in nums:
        outcome = how_sum_easy(target - modifier, nums)
        if outcome is not False:
            return [modifier] + outcome

    return False


def how_sum_manual(target, nums, memo={}):
    # print(memo)
    # base cases
    if target == 0:
        return []
    if target < 0:
        return False

    for modifier in nums:
        outcome = how_sum_manual(target - modifier, nums, memo)
        if outcome is not False:
            memo[target] = [modifier] + outcome
            return memo[target]
        else:
            memo[target] = False

    memo[target] = False
    return memo[target]


if __name__ == "__main__":
    print(how_sum_easy(8, (3, 4)))  # true
    print(how_sum_easy(301, (2, 43)))  # true

    print(how_sum_easy(19531, (200, 400)))  # false

    print(how_sum_manual(8, (3, 4)))  # true
    print(how_sum_manual(301, (2, 43)))  # true

    print(how_sum_manual(1953, (200, 400)))  # false
