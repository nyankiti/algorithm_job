from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())

    def rec(x):
        if x == 0:
            return 1
        else:
            return x*rec(x-1)
    print(rec(N))


if __name__ == '__main__':
    main()
