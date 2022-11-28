from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    S = [list(input()) for _ in range(H)]
    S_count = []
    T = [list(input()) for _ in range(H)]
    T_count = []

    for i in range(H):
        S_count.append(S[i].count("#"))
        T_count.append(T[i].count("#"))

    for i in range(H):
        if S_count[i] != T_count[i]:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    main()
