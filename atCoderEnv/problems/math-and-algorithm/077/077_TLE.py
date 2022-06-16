from sys import stdin


def get_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def main():
    N = int(stdin.readline())
    points = []
    for _ in range(N):
        X, Y = map(int, stdin.readline().split())
        points.append([X, Y])

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += get_distance(points[i], points[j])
    print(ans)


if __name__ == '__main__':
    main()
