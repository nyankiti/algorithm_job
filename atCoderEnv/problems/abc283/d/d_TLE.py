from sys import stdin, setrecursionlimit, exit
from collections import defaultdict, deque

setrecursionlimit(10**6)


def check(s):
    pass


def main():
    S = input()
    # 愚直に探索する
    hako = deque()
    hako_visited = defaultdict(bool)
    # "(" が出現するindexをdequeで管理
    dq = deque()
    for i in range(len(S)):
        if S[i] == "(":
            dq.append(i)
        elif S[i] == ")":
            j = dq.pop()
            for k in range(j, i):
                hako_visited[S[k]] = False
                if hako:
                    hako.pop()
        else:
            if hako_visited[S[i]]:
                print("No")
                exit()
            else:
                hako.append(S[i])
                hako_visited[S[i]] = True
    print("Yes")


if __name__ == '__main__':
    main()
