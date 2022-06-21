from sys import stdin


def main():
    N = int(stdin.readline())

    points = []
    for i in range(N):
        C, P = map(int, stdin.readline().split())
        points.append([C, P])

    Q = int(stdin.readline())
    for _ in range(Q):
        L, R = map(int, stdin.readline().split())
        li = points[L-1:R]
        first_sum = 0
        second_sum = 0
        for el in li:
            if el[0] == 1:
                first_sum += el[1]
            elif el[0] == 2:
                second_sum += el[1]

        print(first_sum, second_sum)


if __name__ == '__main__':
    main()
