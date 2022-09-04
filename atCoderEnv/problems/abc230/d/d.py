from sys import stdin


def main():
    N, D = map(int, stdin.readline().split())
    walls = []
    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        walls.append([L, R])

    walls.sort(key=lambda x: x[1])
    i = 0
    count = 0
    start_pos = walls[i][1]

    while i < N:
        start_pos = walls[i][1]
        count += 1

        while i < N and walls[i][0] < start_pos+D:
            i += 1
    print(count)


if __name__ == '__main__':
    main()
