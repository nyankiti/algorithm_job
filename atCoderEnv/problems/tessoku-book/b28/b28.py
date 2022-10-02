from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    N = int(stdin.readline())
    dp = [0]*(N+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    print(dp[-1])


if __name__ == '__main__':
    main()
