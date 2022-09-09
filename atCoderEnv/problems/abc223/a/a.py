from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    X = int(stdin.readline())
    if X % 100 == 0 and X != 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
