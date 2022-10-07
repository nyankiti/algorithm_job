from collections import deque
from sys import stdin, setrecursionlimit, exit

setrecursionlimit(10**6)


def main():
    N, S = map(int, stdin.readline().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, stdin.readline().split())
        A.append(a)
        B.append(b)

    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True

    for i in range(1, N+1):
        for j in range(S+1):
            if j-A[i-1] >= 0:
                dp[i][j] = dp[i-1][j-A[i-1]] or dp[i][j]
            if j-B[i-1] >= 0:
                dp[i][j] = dp[i-1][j-B[i-1]] or dp[i][j]

    for row in dp:
        print(row)

    if dp[N][S] == False:
        print("No")
        return

    # 復元する
    dq = deque()

    def rec(i, s):
        if i == 0 and s == 0:
            print("".join(reversed(dq)))
            exit()
        if dp[i-1][s-A[i-1]]:
            dq.append("H")
            rec(i-1, s-A[i-1])
            dq.pop()

        if dp[i-1][s-B[i-1]]:
            dq.append("T")
            rec(i-1, s-B[i-1])
            dq.pop()
    print("Yes")
    rec(N, S)


if __name__ == '__main__':
    main()
