from sys import stdin, exit
from collections import deque

N = int(stdin.readline())

if N % 2 == 1:
    print()
    exit()

# 2 ^ N 通りなので、bit全探索する


def check_valid_parentheses(parentheses: deque):
    temp_dq = parentheses.copy()
    check_dq = deque()
    while temp_dq:
        poped = temp_dq.popleft()
        if poped == ")":
            if check_dq:
                check_dq_popped = check_dq.pop()
                if check_dq_popped == "(":
                    continue
                else:
                    # check_dq.append(check_dq_popped)
                    #  ")"が連続してcheck_dqに入る場合、正しいparenthesesでないことが確定するので、Falseをreturnする
                    return False
            else:
                # check_dq.append(poped)
                return False
        else:
            check_dq.append(poped)

    return False if check_dq else True


for i in range(2 ** N):
    dq = deque()
    for j in range(N):
        if ((i >> j) & 1):
            dq.appendleft(")")
        else:
            dq.appendleft("(")

    if check_valid_parentheses(dq):
        print("".join(dq))
