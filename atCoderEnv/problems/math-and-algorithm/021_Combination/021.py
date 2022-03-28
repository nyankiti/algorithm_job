from sys import stdin

n, r = map(int, stdin.readline().split())


def permutation(n, r, position):
    if position == n - r:
        return 1
    return position * permutation(n, r, position-1)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def combination(n, r):
    return permutation(n, r, n) // factorial(r)
    # 順列は _nP_1 であるので、以下のように書き換えることもできる
    # return permutation(n, r, n) // permutation(r, 1, r)


print(combination(n, r))
