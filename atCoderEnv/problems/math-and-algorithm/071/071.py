from sys import stdin

"""
それぞれの交点を求め、条件に適しているかを判定する
"""


def intersection_point(a_1, b_1, c_1, a_2, b_2, c_2):
    x = (c_1*b_2 - c_2*b_1)/(a_1*b_2 - a_2*b_1)
    y = (c_1*a_2 - c_2*a_1)/(b_1*a_2 - b_2*a_1)
    return [x, y]


def main():
    N = int(stdin.readline())

    conditions = []
    for _ in range(N):
        a, b, c = map(int, stdin.readline().split())
        conditions.append((a, b, c))

    def check(point):
        for condition in conditions:
            if point[0] * condition[0] + point[1]*condition[1] > condition[2]:
                return False
        return True

    intersections = []
    for i in range(N):
        for j in range(N):
            if i != j:
                temp = intersection_point(conditions[i][0], conditions[i][1], conditions[i]
                                          [2], conditions[j][0], conditions[j][1], conditions[j][2])

                intersections.append(temp)

    ans = -10000000
    for point in intersections:
        if check(point):
            ans = max(point[0]+point[1], ans)

    print(ans)


if __name__ == '__main__':
    main()
