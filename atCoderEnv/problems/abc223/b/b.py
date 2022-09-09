from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    dq = deque()
    dq.extend(list(S))
    max_ans = S
    min_ans = S

    for _ in range(len(S)):
        temp = "".join(dq)
        max_ans = max(max_ans, temp)
        min_ans = min(min_ans, temp)

        poped = dq.pop()
        dq.appendleft(poped)

    print(min_ans)
    print(max_ans)


if __name__ == '__main__':
    main()
