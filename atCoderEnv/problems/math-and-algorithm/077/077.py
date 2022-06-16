from sys import stdin


def get_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def main():
    N = int(stdin.readline())
    Xs = []
    Ys = []
    for _ in range(N):
        X, Y = map(int, stdin.readline().split())
        Xs.append(X)
        Ys.append(Y)

    Xs.sort()
    Ys.sort()

    ans = 0

    for i in range(N):
        ans += Xs[i] * (-N + 2*i + 1)
        ans += Ys[i] * (-N + 2*i + 1)

    print(ans)


if __name__ == '__main__':
    main()
