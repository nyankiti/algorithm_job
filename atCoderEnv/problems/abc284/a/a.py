from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S = [input() for _ in range(N)]
    for s in reversed(S):
        print(s)


if __name__ == '__main__':
    main()
