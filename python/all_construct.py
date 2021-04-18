# Given the same predicates as the previous problem (can-construct)
# We want the all the ways we can construct a string

from functools import cache


@cache
def all_construct_easy(target, bank):
    if target == "":
        return [[]]

    accum = []
    for word in bank:
        if target.startswith(word):
            new_target = target[len(word):]
            for result in all_construct_easy(new_target, bank):
                accum.append([word, *result])

    return accum


def all_construct_manual(target, bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    accum = []
    for word in bank:
        if target.startswith(word):
            new_target = target[len(word):]
            for result in all_construct_manual(new_target, bank, memo):
                accum.append([word, *result])

    memo[target] = accum
    return accum


if __name__ == "__main__":
    print(all_construct_easy("abcdef", ("ab", "abc", "cd", "def", "abcd", "ef")))
    print(all_construct_easy("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ("e", "ee", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee")))

    print(all_construct_manual("abcdef", ("ab", "abc", "cd", "def", "abcd", "ef"), {}))
    print(all_construct_manual("eeeeeeeeef", ("e", "ee", "f"), {}))
