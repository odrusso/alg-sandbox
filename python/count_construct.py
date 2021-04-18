# Given the same predicates as the previous problem (can-construct)
# We want the number of ways that we can construct the string.

from functools import cache


@cache
def count_construct_easy(target, bank):
    if target == "":
        return 1

    accum = 0
    for word in bank:
        if target.startswith(word):
            new_target = target[len(word):]
            accum += count_construct_easy(new_target, bank)

    return accum


def count_construct_manual(target, bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    accum = 0
    for word in bank:
        if target.startswith(word):
            new_target = target[len(word):]
            accum += count_construct_easy(new_target, bank)

    memo[target] = accum
    return accum


if __name__ == "__main__":
    print(count_construct_easy("abcdef", ("ab", "abc", "cd", "def", "abcd", "ef")))
    print(count_construct_easy("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "f")))

    print(count_construct_manual("abcdef", ("ab", "abc", "cd", "def", "abcd", "ef"), {}))
    print(count_construct_manual("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "f"), {}))
    # This will have something like 37^8 nodes in the call tree, ~3512479453921
