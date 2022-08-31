from sys import stdin


def main():
    X, Y, N = map(int, stdin.readline().split())

    if X*3 < Y:
        # 3個まとめて買ってもお得にならない場合
        print(N*X)
    else:
        print(N//3 * Y + N % 3 * X)


if __name__ == '__main__':
    main()
