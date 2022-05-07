from sys import stdin, exit


def main():
    N, M = map(int, stdin.readline().split())
    neighbors = [[] for _ in range(N+1)]

    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        neighbors[A].append(B)
        neighbors[B].append(A)

        if len(neighbors[A]) > 2 or len(neighbors[B]) > 2:
            print("No")
            exit()
        # 境界条件
        if A == 1 or A == N:
            if len(neighbors[A]) > 1:
                print("No")
                exit()
        if B == 1 or B == N:
            if len(neighbors[B]) > 1:
                print("No")
                exit()

    print("Yes")


if __name__ == '__main__':
    main()
