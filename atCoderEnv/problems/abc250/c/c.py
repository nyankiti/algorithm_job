from sys import stdin


def main():
    N, Q = map(int, stdin.readline().split())
    numbers = list(range(1, N+1))

    # indexの変更を記憶する
    memo = {}
    for i in range(1, N+1):
        memo[i] = i

    for _ in range(Q):
        x = int(stdin.readline())
        # memoのチェック
        y = memo.get(x)

        if y == N:
            # 右端の場合
            numbers[y-1], numbers[y-2] = numbers[y-2], numbers[y-1]

            memo[numbers[y-1]] = y
            memo[numbers[y-2]] = y-1
        else:
            numbers[y-1], numbers[y] = numbers[y], numbers[y-1]

            memo[numbers[y-1]] = y
            memo[numbers[y]] = y+1
        # print(numbers)
    print(*numbers)


if __name__ == '__main__':
    main()
