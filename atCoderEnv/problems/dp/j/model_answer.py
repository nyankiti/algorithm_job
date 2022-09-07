from collections import Counter
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    c = Counter(A)

    # dp[c1][c2][c3] := 1個残りがc1個, 2個残りがc2個, 3個残りがc3個である状態にするまでの操作回数の期待値
    dp = [[[0]*(N+2) for _ in range(N+2)] for _ in range(N+2)]
    '''
    dp[c1][c2][c3] = 
    dp[c1-1][c2][c3] * (1個の皿が選ばれる確率)
                       +
    dp[c1+1][c2-1][c3] * (2個の皿が選ばれる確率)
                       +
    dp[c1][c2+1][c3-1] * (3個の皿が選ばれる確率)
                       +
    dp[c1][c2][c3] * (0個の皿が選ばれる確率) 

    0個の皿が選ばれる確率の項を移項して完成。
    '''

    # c1 から回していくのがポイント
    for c3 in range(N+1):
        for c2 in range(N+1):
            for c1 in range(N+1):
                c_sum = c1+c2+c3
                # c_sum > N の条件を忘れるとTLEするので注意
                if c_sum == 0 or c_sum > N:
                    continue
                temp = N/c_sum
                if c1 > 0:
                    temp += dp[c1-1][c2][c3] * c1/c_sum
                if c2 > 0:
                    temp += dp[c1+1][c2-1][c3] * c2/c_sum
                if c3 > 0:
                    temp += dp[c1][c2+1][c3-1] * c3/c_sum
                dp[c1][c2][c3] = temp

    # print(c)
    print(dp[c[1]][c[2]][c[3]])

    # for c1 in range(N):
    #     for c2 in range(N):
    #         for c3 in range(N):
    #             print(
    #                 f"c1: {c1}, c2: {c2}, c3: {c3}, expectation: {dp[c1][c2][c3]}")


if __name__ == '__main__':
    main()
