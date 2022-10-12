from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    dq = deque()
    for i, val in enumerate(S):
        if dq and dq[-1][0] == "(" and val == ")":
            print(dq.pop()[1], i+1)
        else:
            dq.append([val, i+1])


if __name__ == '__main__':
    main()
