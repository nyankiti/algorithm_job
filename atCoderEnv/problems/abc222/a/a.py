from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = input()

    while len(N) < 4:
        N = "0" + N
    print(N)


if __name__ == '__main__':
    main()
