from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    ans = 0

    dq = deque()

    dq.append(A[0])
    i = 1
    while i < N:
        dq.append(A[i])
        if dq[-1] - dq[0] <= K:
            ans += 1
        else:
            dq.popleft()

            while dq and dq[-1] - dq[0] > K:
                dq.pop()
                i -= 1
            ans += (len(dq)-1)
        i += 1

    # 先頭の数字はすでにカウント済みなので、先頭以外の数字で作れるペアの数を ans に加える
    rest = len(dq) - 1
    ans += rest*(rest-1)//2
    print(ans)


if __name__ == '__main__':
    main()
