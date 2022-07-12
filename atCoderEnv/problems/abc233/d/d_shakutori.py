from sys import stdin
from collections import deque


# しゃくとり法 => 負数があるので、左のポインターを動かすタイミングを決めれない
def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    dq = deque()
    temp_sum = 0
    ans = 0

    for a in A:
        dq.append(a)
        temp_sum += a

        if temp_sum == K:
            ans += 1

        while dq and temp_sum > K:
            rm = dq.popleft()
            temp_sum -= rm

            if temp_sum == K:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
