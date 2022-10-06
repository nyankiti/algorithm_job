from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    a, b, c = map(int, stdin.readline().split())
    if (a+b+c == 0):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
