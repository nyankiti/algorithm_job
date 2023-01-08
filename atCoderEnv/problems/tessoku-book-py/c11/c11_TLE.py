from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    # 愚直に解いてみる(TLEするはず)
    li = []
    for i in range(1, max(K, N)):
        for j, a in enumerate(A):
            li.append([j+1, a//i])
    li.sort(key=lambda x: x[1], reverse=True)

    ans = defaultdict(int)
    for i in range(K):
        ans[li[i][0]] += 1

    for i in range(N):
        print(ans[i+1], end=" ")


if __name__ == '__main__':
    main()
