from sys import stdin


def main():
    N = int(stdin.readline())

    first_accumulative_sum = [0]
    second_accumulative_sum = [0]
    for i in range(N):
        C, P = map(int, stdin.readline().split())
        if C == 1:
            first_accumulative_sum.append(first_accumulative_sum[-1] + P)
            second_accumulative_sum.append(second_accumulative_sum[-1])
        elif C == 2:
            second_accumulative_sum.append(second_accumulative_sum[-1] + P)
            first_accumulative_sum.append(first_accumulative_sum[-1])

    Q = int(stdin.readline())
    for _ in range(Q):
        L, R = map(int, stdin.readline().split())
        first_ans = first_accumulative_sum[R] - first_accumulative_sum[L-1]
        second_ans = second_accumulative_sum[R] - second_accumulative_sum[L-1]
        print(first_ans, second_ans)


if __name__ == '__main__':
    main()
