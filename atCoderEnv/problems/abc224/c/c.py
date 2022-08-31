from sys import stdin


def is_same_line(point1, point2, point3):
    # # まずpoint1とpoint2の直線の式を作る
    # if point2[0] - point1[0] == 0:
    #     return point1[0] == point3[0]
    # else:
    #     # 傾き a
    #     a = (point2[1] - point1[1])/(point2[0] - point1[0])

    #     # 直線の式は、y - point1[1] = a(x - point1[0]) となる。
    #     # よって、point3 がこの直線上の点かどうかを確かめるには、、
    #     return point3[1] == a*(point3[0] - point1[0]) + point1[1]

    # 除算が絡むと面倒なので、以下のように判定する
    return (point3[1] - point1[1])*(point2[0]-point1[0]) == (point2[1] - point1[1])*(point3[0] - point1[0])


def main():
    N = int(stdin.readline())
    points = []
    for _ in range(N):
        X, Y = map(int, stdin.readline().split())
        points.append([X, Y])

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if is_same_line(points[i], points[j], points[k]):
                    count += 1
    nC3 = N*(N-1)*(N-2)//6
    print(nC3-count)


if __name__ == '__main__':
    main()
