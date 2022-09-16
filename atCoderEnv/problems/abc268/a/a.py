from collections import Counter
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    *A, = map(int, stdin.readline().split())
    c = Counter(A)
    print(len(c.keys()))


if __name__ == '__main__':
    main()
