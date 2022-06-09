from sys import stdin, exit
from collections import deque

N = int(stdin.readline())

if N % 2 == 1:
    print()
    exit()

# 2 ^ N 通りなので、bit全探索する


def check_valid_parentheses(parentheses):
    judge_num = 0
    for el in parentheses:
        if el == "(":
            judge_num += 1
        elif el == ")":
            judge_num -= 1

        if judge_num < 0:
            return False
    if judge_num == 0:
        return True
    else:
        return False


for i in range(2 ** N):
    canditate = ["" for _ in range(N)]
    for j in range(N):
        if ((i >> j) & 1):
            canditate[N - j - 1] = ")"
        else:
            canditate[N - j - 1] = "("

    if check_valid_parentheses(canditate):
        print("".join(canditate))
