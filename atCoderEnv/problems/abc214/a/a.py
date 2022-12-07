from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    if N <= 125:
        print(4)
    elif N <= 211:
        print(6)
    else:
        print(8)


if __name__ == '__main__':
    main()
