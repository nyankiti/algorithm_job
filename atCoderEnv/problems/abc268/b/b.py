from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    T = input()

    if S == T[:len(S)]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
