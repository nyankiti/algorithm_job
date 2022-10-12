from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, Q = map(int, stdin.readline().split())
    S = input()
    for _ in range(Q):
        a, b, c, d = map(int, stdin.readline().split())
        if S[a-1:b] == S[c-1:d]:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
