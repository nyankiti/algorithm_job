from sys import stdin


def main():
    N, M, X, T, D = map(int, stdin.readline().split())

    if M > X:
        print(T)
    else:
        print(T - (X-M)*D)


if __name__ == '__main__':
    main()
