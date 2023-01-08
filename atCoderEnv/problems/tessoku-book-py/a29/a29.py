from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    a, b = map(int, stdin.readline().split())
    print(pow(a, b, MOD))


if __name__ == '__main__':
    main()
