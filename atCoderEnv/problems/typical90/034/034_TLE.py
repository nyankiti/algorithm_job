from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    ans = 0
    # 愚直な全探索
    for i in range(N):
        k = 0
        counter = defaultdict(bool)
        j = i
        temp_ans = 0
        while k <= K and j < N:
            if counter[A[j]]:
                j += 1
                temp_ans += 1
            else:
                counter[A[j]] = True
                k += 1
        ans = max(ans, temp_ans)
    print(ans)


if __name__ == '__main__':
    main()
