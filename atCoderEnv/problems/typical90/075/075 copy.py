from sys import stdin
import math
from collections import deque

from numpy import append

N = int(stdin.readline())


def is_prime(x):
    if x % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False

    return True


def divied_big_two_factor(x):
    factors = []
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            # ニ乗の場合
            if i == x // i:
                return (i, i)

            factors.append(i)
            factors.append(x // i)

    if len(factors) < 2:
        return 2, 2

    return (factors[-1], factors[-2])


def magic(balls):
    temp_balls = []
    for ball in balls:
        if not is_prime(ball):
            temp_balls.append(ball)

    if len(temp_balls) == 0:
        # 全て素数であるので終了する
        return False

    new_balls = []
    for new_ball in temp_balls:
        x, y = divied_big_two_factor(new_ball)
        new_balls.append(x)
        new_balls.append(y)

    return new_balls


balls = []
balls.append(N)
ans = 0

while balls:
    balls = magic(balls)
    ans += 1

print(ans - 1)
