from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, X, Y = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # dp[i] => i番目にいる可能性のある座用の配列
    dp = [[] for _ in range(N+1)]
    dp[0].append((0, 0))
    dp[1].append((A[0], 0))

    for i in range(1, N):
        # 2**N乗まで伸びてしまうのでTLE
        for x, y in dp[i]:
            if i % 2 == 0:
                dp[i+1].append((x+A[i], y))
                dp[i+1].append((x-A[i], y))
            else:
                dp[i+1].append((x, y+A[i]))
                dp[i+1].append((x, y-A[i]))
    print(len(dp[-1]))
    if (X, Y) in dp[-1]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
