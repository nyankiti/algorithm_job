from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    ruiseki = [0]
    temp_sum = 0
    for a in A:
        temp_sum += a
        ruiseki.append(temp_sum)

    def get_sum(l, r):
        return ruiseki[r] - ruiseki[l-1]
    # しゃくとり法
    R = [0]*100009
    for i in range(1, N+1):
        if i == 1:
            R[i] = 0
        else:
            R[i] = R[i-1]

        while R[i] < N and get_sum(i, R[i]+1) <= K:
            R[i] += 1

    # 答えを求める
    ans = 0
    for i in range(1, N+1):
        ans += (R[i] - i + 1)

    print(ans)


if __name__ == '__main__':
    main()
