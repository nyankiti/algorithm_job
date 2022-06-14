from sys import stdin


def main():
    R, C = map(int, stdin.readline().split())
    matrix = []

    for _ in range(2):
        a_1, a_2 = map(int, stdin.readline().split())
        matrix.append([a_1, a_2])

    print(matrix[R-1][C-1])


if __name__ == '__main__':
    main()
