from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S, T = input().split()
    if S > T:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
