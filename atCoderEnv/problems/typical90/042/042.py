from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
MOD = 10**9 + 7


def main():
    K = int(stdin.readline())

    if K % 9 != 0:
        print(0)
        return

    """
    桁和が 9 の倍数である数字は自動的にその数字自体も9の倍数になるところがポイント。
    
    よってこの問題は、9の倍数かどうかを考えずに、桁和が K になる数の通り数を数える作業となる。
    => 桁和が K になる数の通り数を数える場合は、dpが便利。
    """

    dp = [0]*(K+1)
    dp[0] = 1

    for i in range(1, K+1):
        for j in range(1, 10):
            if i - j >= 0:
                dp[i] += dp[i-j]
        dp[i] %= MOD
    print(dp[-1])


if __name__ == '__main__':
    main()
