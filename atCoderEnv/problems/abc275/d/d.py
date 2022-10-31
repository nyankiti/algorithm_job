from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())

    lookup = {}

    def rec(n):
        if n in lookup:
            return lookup[n]
        if n == 0:
            return 1

        lookup[n] = rec(int(n/2)) + rec(int(n/3))
        return lookup[n]

    print(rec(N))


if __name__ == '__main__':
    main()
