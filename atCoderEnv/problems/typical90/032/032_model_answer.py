from itertools import permutations
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    A = []
    for _ in range(N):
        *a, = map(int, stdin.readline().split())
        A.append(a)
    M = int(stdin.readline())

    # 仲が良い時、False, 仲が悪い時Trueとなる、部員の関係を表した行列
    relations = [[False]*N for _ in range(N)]
    for _ in range(M):
        x, y = map(int, stdin.readline().split())
        relations[x-1][y-1] = True
        relations[y-1][x-1] = True

    result = []
    for perm in permutations(range(N)):
        time = A[perm[0]][0]
        for i in range(1, N):
            if relations[perm[i]][perm[i-1]]:
                break
            time += A[perm[i]][i]
            if i == N-1:
                result.append(time)

    if N == 1:
        result.append(A[0][0])

    if len(result) == 0:
        print(-1)
    else:
        print(min(result))


if __name__ == '__main__':
    main()
