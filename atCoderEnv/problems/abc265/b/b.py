from sys import stdin


def main():
    N, M, T = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    bonus = {}
    for _ in range(M):
        X, Y = map(int, stdin.readline().split())
        bonus[X] = Y

    for i in range(1, N):
        T += bonus.get(i, 0)

        if T > A[i-1]:
            T -= A[i-1]
        else:
            break

    else:
        print("Yes")
        return

    print("No")


if __name__ == '__main__':
    main()
