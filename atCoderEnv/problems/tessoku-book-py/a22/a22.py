from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    # 配る方法が不確定(どのマスから遷移する可能性があるかはわからない)なので、送るDPをする
    min_inf = -1000
    dp = [min_inf]*N
    dp[0] = 0
    for i in range(N-1):
        # その時点での最大を取っても後から最大じゃなくなる場合がある
        dp[A[i]-1] = max(dp[A[i]-1], dp[i]+100)
        dp[B[i]-1] = max(dp[B[i]-1], dp[i]+150)
    print(dp[-1])


if __name__ == '__main__':
    main()
