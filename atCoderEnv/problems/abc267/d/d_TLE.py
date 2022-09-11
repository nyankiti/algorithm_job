from itertools import combinations
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

# N < 2000 なので、O(N^2)まではいける


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # O(N^2)まで許容されるので、全探索できそう
    # dp = [[-1]*N for _ in range(N)]

    ans = -1
    for comb in combinations(A, M):
        temp = 0
        for i, v in enumerate(comb):
            temp += (i+1)*v
        ans = max(ans, temp)
    print(ans)


if __name__ == '__main__':
    main()
