from sys import stdin


def main():
    N, X, Y = map(int, stdin.readline().split())

    dp_red = [0]*(N+1)
    dp_blue = [0]*(N+1)

    dp_red[N] = 1

    for i in range(N, 1, -1):
        # if dp_red[i] > 0:
        n = dp_red[i]
        dp_red[i] -= n
        dp_red[i-1] += n
        dp_blue[i] += X*n

        # if dp_blue[i] > 0:
        n = dp_blue[i]
        dp_blue[i] -= n
        dp_red[i-1] += n
        dp_blue[i-1] += Y*n

    print(dp_blue[1])


if __name__ == '__main__':
    main()
