from sys import stdin
import math


def main():
    N = int(stdin.readline())
    points = []
    ans = math.inf
    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        for point in points:
            distance = math.sqrt((point[0] - x)**2 + (point[1] - y)**2)
            if distance < ans:
                # print(point[0], point[1], "と", x, y, "の距離")
                ans = distance
        points.append((x, y))
    print(ans)


if __name__ == '__main__':
    main()
