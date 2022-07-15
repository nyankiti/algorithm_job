from sys import stdin, exit


def main():
    N, M = map(int, stdin.readline().split())
    B = [list(map(int, stdin.readline().split())) for _ in range(N)]
    Bt = list(zip(*B))

    for row in B:
        for i in range(len(row) - 1):
            if row[i+1] - row[i] != 1:
                print("No")
                exit()

            if row[i] % 7 == 0 and row[i+1] % 7 == 1:
                print("No")
                exit()

    for row in Bt:
        for i in range(len(row) - 1):
            if row[i+1] - row[i] != 7:
                print("No")
                exit()

    print("Yes")


if __name__ == '__main__':
    main()
