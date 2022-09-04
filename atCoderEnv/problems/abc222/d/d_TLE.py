from sys import stdin
import bisect

MOD = 998244353


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    diff_li = []

    for i in range(N):
        diff_li.append(list(range(A[i], B[i]+1, 1)))

    # 一つ前の状態を [可能性のある数字, その数字をとる方法の数] という形式で保存
    dp = [[] for _ in range(N)]
    dp[0] = [[val, 1] for val in diff_li[0]]

    for i in range(1, N):
        diff = diff_li[i]

        for el in diff:
            temp_count = 0
            for prev_el in dp[i-1]:
                if prev_el[0] <= el:
                    temp_count += prev_el[1]
            dp[i].append([el, temp_count])

    # for row in dp:
    #     print(row)
    ans = 0
    for val in dp[-1]:
        ans = (ans + val[1]) % MOD
    print(ans)


if __name__ == '__main__':
    main()
