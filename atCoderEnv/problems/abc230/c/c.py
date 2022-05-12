from sys import stdin


def main():
    N, A, B = map(int, stdin.readline().split())
    P, Q, R, S = map(int, stdin.readline().split())

    # N_grid = [["."]*(N+1) for _ in range(N+1)]
    ans_grid = [["."]*(S-R+1) for _ in range(Q-P+1)]

    # まず、N*Nマス全てを条件に合うように塗る処理も補助として実装する(N*NはmemoryErrorになるので提出はできない)
    k_start = max(1-A, 1-B)
    k_end = min(N-A, N-B)

    for k in range(k_start, k_end+1):
        # N_grid[A+k][B+k] = "#"
        if P <= A+k and A+k <= Q and R <= B+k and B+k <= S:
            ans_grid[A+k-P][B+k-R] = "#"

    k_start = max(1-A, B-N)
    k_end = min(N-A, B-1)

    for k in range(k_start, k_end+1):
        # N_grid[A+k][B-k] = "#"
        if P <= A+k and A+k <= Q and R <= B-k and B-k <= S:
            ans_grid[A+k-P][B-k-R] = "#"

    for row in ans_grid:
        print("".join(row))

    # for row in N_grid:
    #     print(row)


if __name__ == '__main__':
    main()
