from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    A, B = map(int, stdin.readline().split())
    print(A**B)


if __name__ == '__main__':
    main()
