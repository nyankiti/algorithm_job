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

    for i in range(N+1):
        for j in range(i, N+1):
            if cumulative_sum[j] - cumulative_sum[i] == K:
                print(i, cumulative_sum[i], j, cumulative_sum[j])
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
