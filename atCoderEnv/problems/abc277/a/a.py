from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, X = map(int, stdin.readline().split())
    *P, = map(int, stdin.readline().split())

    for i, p in enumerate(P):
        if p == X:
            print(i+1)


if __name__ == '__main__':
    main()
