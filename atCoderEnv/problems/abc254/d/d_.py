import math
from sys import stdin


def calc(square_N, N):
    count = 1
    for i in range(1, N):
        if square_N % i == 0:
            count += 2

    print(N, square_N, count)
    return count


def main():
    N = int(stdin.readline())
    # N = 5

    # 最初に1の分を追加しておく
    ans = 1
    for i in range(2, N):
        ans += calc(i*i, i)

    print(ans)


if __name__ == '__main__':
    main()
