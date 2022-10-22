from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    tree = [[] for _ in range(N)]
    for i, a in enumerate(A):
        # Aはa_2から始まるので、頂点番号を一つずらす必要がある
        v = i+1
        tree[a-1].append(v)

    dp = [0]*N
    for i in range(N-1, -1, -1):
        for sub_v in tree[i]:
            dp[i] += dp[sub_v]+1
    print(*dp)


if __name__ == '__main__':
    main()
