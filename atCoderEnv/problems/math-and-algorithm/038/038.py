from sys import stdin


def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    temp_sum = 0
    cumulative_sum = [0]
    for i in range(N):
        temp_sum += A[i]
        cumulative_sum.append(temp_sum)

    for _ in range(Q):
        L, R = map(int, stdin.readline().split())
        # print(R, ":", cumulative_sum[R])
        # print(L, ":", cumulative_sum[L])
        print(cumulative_sum[R] - cumulative_sum[L-1])


if __name__ == '__main__':
    main()
