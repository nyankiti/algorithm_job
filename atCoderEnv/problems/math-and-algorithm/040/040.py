from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    cumulative_sum = [0]
    temp_sum = 0
    for a in A:
        temp_sum += a
        cumulative_sum.append(temp_sum)

    # print(cumulative_sum)

    M = int(stdin.readline())
    prev_station = int(stdin.readline())
    ans = 0
    for _ in range(M-1):
        B = int(stdin.readline())

        # print(B, abs(cumulative_sum[B-1] - cumulative_sum[prev_station-1]))
        ans += abs(cumulative_sum[B-1] - cumulative_sum[prev_station-1])
        prev_station = B
    print(ans)


if __name__ == '__main__':
    main()
