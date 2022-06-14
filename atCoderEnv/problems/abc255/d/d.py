from sys import stdin
import bisect


def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    # 累積和を前計算しておく
    A.sort()
    cumulative_sum = [0]
    temp_sum = 0
    for a in A:
        temp_sum += a
        cumulative_sum.append(temp_sum)

    # print(A)
    # print(cumulative_sum)
    for _ in range(Q):
        X = int(stdin.readline())
        k = bisect.bisect_right(A, X)
        # print("X", X, "k", k)
        # print("k*X", k*X, "cumulative_sum[k]", cumulative_sum[k])
        # print((cumulative_sum[N]-cumulative_sum[k]), "(N-k)*X", (N-k-1)*X)
        ans = k*X - cumulative_sum[k]
        ans = ans + (cumulative_sum[N]-cumulative_sum[k]) - (N-k)*X
        print(ans)


if __name__ == '__main__':
    main()
