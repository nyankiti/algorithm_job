from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    # i日目に勉強する場合の実力最大値
    dp_1 = [0]*(N+1)
    # i日目に勉強しない場合の実力最大値
    dp_2 = [0]*(N+1)

    for i in range(1, N+1):
        dp_1[i] = dp_2[i-1] + A[i-1]
        dp_2[i] = max(dp_1[i-1], dp_2[i-1])

    print(max(dp_1[-1], dp_2[-1]))


if __name__ == '__main__':
    main()
