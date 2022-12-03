from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    k = 0
    num = 2
    while num <= N:
        k += 1
        num *= 2
    print(k)


if __name__ == '__main__':
    main()
