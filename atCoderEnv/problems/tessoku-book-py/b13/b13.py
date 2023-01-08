from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    ans = 0
    dq = deque()
    temp_sum = 0

    # 左を基準としたしゃくとり
    for i, a in enumerate(A):
        if len(dq) == 0:
            dq.append(a)
            temp_sum += a

        while temp_sum <= K:
            if i+len(dq) < N:
                next_a = A[i+len(dq)]
                if temp_sum + next_a <= K:
                    dq.append(next_a)
                    temp_sum += next_a
                else:
                    break
            else:
                break

        if temp_sum <= K:
            ans += len(dq)
        temp_sum -= dq.popleft()

    print(ans)


if __name__ == '__main__':
    main()
