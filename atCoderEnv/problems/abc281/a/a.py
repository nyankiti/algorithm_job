from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    for i in range(N, -1, -1):
        print(i)


if __name__ == '__main__':
    main()
