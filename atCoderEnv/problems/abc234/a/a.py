from sys import stdin

t = int(input())


def func(t: int):
    return t**2 + 2 * t + 3


result = func(func(func(t) + t) + func(func(t)))
print(result)
