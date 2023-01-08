from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    # 二つのdpを使う(i日目に勉強する場合としない場合)
    dp = [0]*N
    dp_not = [0]*N
    dp[0] = A[0]
    for i in range(1, N):
        dp[i] = max(dp_not[i-1], dp[i-2]) + A[i]
        dp_not[i] = max(dp_not[i-1], dp[i-1])
    print(max(dp[-1], dp_not[-1]))


if __name__ == '__main__':
    main()
