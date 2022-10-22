from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S = input()
    print("Yes" if S[N-1] == "o" else "No")


if __name__ == '__main__':
    main()
