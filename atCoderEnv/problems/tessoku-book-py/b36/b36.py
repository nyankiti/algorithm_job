from itertools import count
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    S = input()
    one_count = S.count("1")
    if abs(K-one_count) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
