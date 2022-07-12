from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    ans = 0

    cumulative_sum = [0]
    temp_sum = 0
    for a in A:
        temp_sum += a
        cumulative_sum.append(temp_sum)
    """
    cumulative_sum[r]-cumulative_sum[l-1] = K となる数を、1<l<r の範囲で数えれば良い。(r > lを許さないことに注意)
    よって、cumulative_sum[l-1] = cumulative_sum[r] - K を満たす l の数をcntに保存しておくと計算が早まる
    """

    l_cnt = {}
    for i in range(1, N+1):
        # lの数をメモ
        l_cnt[cumulative_sum[i-1]] = l_cnt.get(cumulative_sum[i-1], 0) + 1

        # r について、条件 cumulative_sum[l-1] = cumulative_sum[r] - K を満たす l の数を取り出す
        ans += l_cnt.get(cumulative_sum[i]-K, 0)
        # print(cnt)
        # print(cnt.get(cumulative_sum[i+1]-K, 0))

    print(ans)


if __name__ == '__main__':
    main()
