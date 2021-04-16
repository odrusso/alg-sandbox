from functools import cache


@cache
def best_sum_easy(target, nums):
    # base cases
    if target == 0:
        return []
    if target < 0:
        return False

    best = False
    for remainder in nums:
        remainder_result = best_sum_easy(target - remainder, nums)
        if remainder_result is not False:
            if not best:
                # the first result we've seen - so it's best by default
                best = [remainder, *remainder_result]
            elif len(remainder_result) < len(best):
                best = [remainder, *remainder_result]
    return best


def best_sum_manual(target, nums, memo={}):
    # base cases
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return False

    best = False
    for remainder in nums:
        remainder_result = best_sum_manual(target - remainder, nums, memo)
        if remainder_result is not False:
            if not best or len(remainder_result) < len(best):
                # the first result we've seen - so it's best by default
                best = [remainder, *remainder_result]

    memo[target] = best
    return best


if __name__ == "__main__":
    print(best_sum_easy(8, (3, 4, 2)))  # 4, 4
    print(best_sum_easy(301, (2, 43)))  # 43 * 7
    print(best_sum_easy(7, (5, 3, 4, 7)))  # true
    print(best_sum_easy(19531, (200, 400)))  # false

    # This code has some issues with memo reuse between runs.
    # The Python GC letting us down!
    print(best_sum_manual(8, (3, 4, 2), {}))  # 4, 4
    print(best_sum_manual(301, (2, 43), {}))  # 43 * 7
    print(best_sum_manual(7, (5, 3, 4, 7), {}))  # true
    print(best_sum_manual(19531, (200, 400), {}))  # false
