from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    print(N//3 + N//5 - N//15)


if __name__ == '__main__':
    main()
