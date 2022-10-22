from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, X, Y = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    A_SUM = sum(A)
    if X + Y > A_SUM and (X+Y) % 2 != A_SUM % 2:
        print("No")
        return

    # direction = 0 の時 => 横、direction = 1 の時 => 縦に進む
    visited = {}

    def dfs(i, x, y, direction, A_sum):
        if (i, x, y) in visited:
            return
        if abs(X-x)+abs(Y-y) > A_sum:
            return

        if i == N:
            if x == X and y == Y:
                print("Yes")
                exit()
        else:
            if direction == 0:
                if abs(X - (x+A[i]))+abs(Y-y) <= A_sum:
                    if (abs(X - (x+A[i]))+abs(Y-y)) % 2 == (A_sum-A[i]) % 2:
                        dfs(i+1, x+A[i], y, 1-direction, A_sum-A[i])
                        visited[(i+1, x+A[i], y)] = True
                if abs(X - (x-A[i]))+abs(Y-y) <= A_sum:
                    if (abs(X - (x-A[i]))+abs(Y-y)) % 2 == (A_sum-A[i]) % 2:
                        dfs(i+1, x-A[i], y, 1-direction, A_sum-A[i])
                        visited[(i+1, x-A[i], y)] = True
            else:
                if abs(Y - (y+A[i]))+abs(X-x) <= A_sum:
                    if (abs(Y - (y+A[i]))+abs(X-x)) % 2 == (A_sum-A[i]) % 2:
                        dfs(i+1, x, y+A[i], 1-direction, A_sum-A[i])
                        visited[(i+1, x, y+A[i])] = True
                if abs(Y - (y-A[i]))+abs(X-x) <= A_sum:
                    if (abs(Y - (y-A[i]))+abs(X-x)) % 2 == (A_sum-A[i]) % 2:
                        dfs(i+1, x, y-A[i], 1-direction, A_sum-A[i])
                        visited[(i+1, x, y-A[i])] = True

    dfs(1, A[0], 0, 1, A_SUM)
    print("No")


if __name__ == '__main__':
    main()
