import math
from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())

    points = []

    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        points.append([x, y])

    def check_count(left, right, down, up):
        count = 0
        for pos in points:
            if pos[0] >= left and pos[0] <= right and pos[1] <= up and pos[1] >= down:
                count += 1
        return count

    ans = math.inf

    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    candidates = [points[i], points[j], points[k], points[l]]
                    left = min(candidates, key=lambda x: x[0])[0]
                    right = max(candidates, key=lambda x: x[0])[0]
                    down = min(candidates, key=lambda x: x[1])[1]
                    up = max(candidates, key=lambda x: x[1])[1]
                    if check_count(left, right, down, up) >= K:
                        area = (right-left)*(up-down)
                        ans = min(ans, area)

    print(ans)


if __name__ == '__main__':
    main()
