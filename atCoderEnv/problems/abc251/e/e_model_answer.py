import math
from sys import stdin


def main():
    N = int(stdin.readline())
    A = [math.inf] + list(map(int, stdin.readline().split()))

    # パターン1 (A1を選ぶ場合 => dp[N]が答え)
    dp = [math.inf for _ in range(N+1)]
    dp[1] = A[1]
    dp[2] = A[1]
    for i in range(3, N+1):
        dp[i] = min(dp[i-2] + A[i-1], dp[i-1] + A[i])

    print(dp)

    temp_ans = dp[N]

    # パターン2 (A_Nを選ぶ場合 => N番目が既に選ばれているので、dp[N-1]が答え)
    dp = [math.inf for _ in range(N+1)]
    dp[0] = A[N]
    dp[1] = A[N]
    for i in range(2, N):
        dp[i] = min(dp[i-2] + A[i-1], dp[i-1] + A[i])

    print(dp)

    print(min(temp_ans, dp[N-1]))


if __name__ == '__main__':
    main()
