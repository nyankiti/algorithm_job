from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    matrix = []
    for _ in range(H):
        *A, = map(int, stdin.readline().split())
        matrix.append(A)

    for i_1 in range(H):
        for i_2 in range(i_1, H):
            for j_1 in range(W):
                for j_2 in range(j_1, W):
                    if matrix[i_1][j_1] + matrix[i_2][j_2] > matrix[i_2][j_1] + matrix[i_1][j_2]:
                        print("No")
                        return
    print("Yes")


if __name__ == '__main__':
    main()
