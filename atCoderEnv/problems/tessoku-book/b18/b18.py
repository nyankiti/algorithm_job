from collections import deque
from sys import stdin, setrecursionlimit, exit

setrecursionlimit(10**6)


def main():
    N, S = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    dp = [[False]*(S+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = True
    for i, a in enumerate(A):
        i += 1
        for j in range(S+1):
            if dp[i-1][j]:
                dp[i][j] = True
            if j - a >= 0 and dp[i-1][j-a]:
                dp[i][j] = True
    # for row in dp:
    #     print(row)

    if dp[-1][-1] == False:
        print(-1)
        return

    path = deque()
    # dfsで経路復元する

    def dfs(i, j):
        if j == 0:
            print(len(path))
            print(*path)
            exit()

        if i <= 0 or j < 0:
            return

        # その数を選んだ
        if 0 <= j-A[i-1] <= S and dp[i-1][j-A[i-1]]:
            path.appendleft(i)
            dfs(i-1, j-A[i-1])
            path.popleft(i)

        # その数を選んでいない
        if dp[i-1][j] == True:
            dfs(i-1, j)

    dfs(N, S)

    # for文で復元
    # j = S
    # for i in range(N, 0, -1):
    #     if 0 <= j-A[i-1] <= S and dp[i-1][j-A[i-1]]:
    #         path.appendleft(i)
    #         j -= A[i-1]

    # while文で復元
    # i = N
    # j = S
    # while True:
    #     if j == 0:
    #         break

    #     # その数を選んだ
    #     if 0 <= j-A[i-1] <= S and dp[i-1][j-A[i-1]]:
    #         path.appendleft(i)
    #         j -= A[i-1]
    #         i -= 1
    #     # その数を選んでいない
    #     elif dp[i-1][j] == True:
    #         i -= 1

    # print(len(path))
    # print(*path)


if __name__ == '__main__':
    main()
