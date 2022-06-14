import math
from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    def calc_distance(x_1, y_1, x_2, y_2):
        row = abs(x_1-x_2)
        col = abs(y_1-y_2)
        return math.sqrt(row*row + col*col)

    points = []
    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        points.append([x, y])

    # それぞれの点から最も近い光を持った点を記録する
    min_distances = []
    for i in range(N):
        temp_min = math.inf
        temp_index = -1
        for a_index, a in enumerate(A):
            dis = calc_distance(
                points[a-1][0], points[a-1][1],  points[i][0], points[i][1])
            if dis < temp_min:
                temp_min = dis
                temp_index = a_index
        min_distances.append([temp_min, temp_index])

    # min_distanceの中で最大値のペアが答えとなる
    ans_index = max(min_distances, key=lambda x: x[0])
    print(ans_index[0])


if __name__ == '__main__':
    main()
