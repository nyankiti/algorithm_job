from sys import stdin, setrecursionlimit, exit
from collections import defaultdict, deque

setrecursionlimit(10**6)


def check(s):
    pass


def main():
    S = input()
    hako_visited = defaultdict(bool)
    dq = deque()
    for i in range(len(S)):
        if S[i] == "(":
            dq.append("(")
        elif S[i] == ")":
            popped = dq.pop()
            while dq and popped != "(":
                hako_visited[popped] = False
                popped = dq.pop()
        else:
            if hako_visited[S[i]]:
                print("No")
                exit()
            else:
                dq.append(S[i])
                hako_visited[S[i]] = True
    print("Yes")


if __name__ == '__main__':
    main()
