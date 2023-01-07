from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            flg = True
            for k in range(M):
                if S[i][k] == "x" and S[j][k] == "x":
                    flg = False
            if flg:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
