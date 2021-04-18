from functools import cache

@cache
def can_construct(target, bank):
    # print(f"case for {target}")
    if target == "":
        return True

    for word in bank:
        # print(f"Checking {target} against {word}")
        if target.startswith(word):
            new_target = target[len(word):]
            child_result = can_construct(new_target, bank)
            if child_result:
                return True

    return False


def can_construct_memo(target, bank, memo):
    # print(f"case for {target}")
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in bank:
        # print(f"Checking {target} against {word}")
        if target.startswith(word):
            new_target = target[len(word):]
            child_result = can_construct_memo(new_target, bank, memo)
            if child_result:
                memo[target] = True
                return True

    memo[target] = False
    return False


if __name__ == "__main__":
    print(can_construct("abcd", ("ab", "cde")))

    print(can_construct_memo("abcdef", ("ab", "cd", "ef"), {}))
    print(can_construct_memo("abcdeeeeabefg", ("ab", "cd", "e", "fg"), {}))
