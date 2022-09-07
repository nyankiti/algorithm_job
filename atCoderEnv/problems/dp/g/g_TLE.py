from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, stdin.readline().split())
        graph[x-1].append(y-1)

    # i番目のノードからの最長パスの長さを格納
    dp = [-1]*N

    def serch(i, path_len):
        if dp[i] != -1:
            return path_len + dp[i]

        sub_ans = path_len
        for adjacent in graph[i]:
            sub_ans = max(sub_ans, serch(adjacent, path_len+1))

        return sub_ans

    ans = -1
    for i in range(N):
        dp[i] = serch(i, 0)
        ans = max(ans, dp[i])

    print(ans)


if __name__ == '__main__':
    main()
