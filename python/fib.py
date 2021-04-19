from functools import cache


@cache
def fib_easy(target):
    if target == 0:
        return 0
    if target == 1:
        return 1

    else:
        return fib_easy(target - 1) + fib_easy(target - 2)


def fib_manual(target, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return 0
    if target == 1:
        return 1

    else:
        memo[target] = fib_manual(target - 1, memo) + fib_manual(target - 2, memo)
        return memo[target]


def fib_tab(target):
    tab = [0 for _ in range(target + 1)]
    tab[1] = 1

    for i in range(target):
        if i < target:
            tab[i+1] += tab[i]
        if i + 1 < target:
            tab[i+2] += tab[i]

    return tab[target]


if __name__ == "__main__":
    print(fib_easy(6))
    print(fib_easy(100))

    print(fib_manual(6))
    print(fib_manual(100))

    print(fib_tab(6))
    print(fib_tab(100))
