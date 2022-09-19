from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    a, b, c, d = map(int, stdin.readline().split())
    print((a+b)*(c-d))
    print("Takahashi")


if __name__ == '__main__':
    main()
