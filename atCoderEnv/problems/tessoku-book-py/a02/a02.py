from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, X = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    print("Yes" if X in A else "No")


if __name__ == '__main__':
    main()
