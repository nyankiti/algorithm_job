import math
from sys import stdin


def main():
    N, L, R = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    ans = math.inf
    # 全探索
    for l in range(N+1):
        for r in range(l, N+1):
            temp = l*L  # 左側の和
            temp += (N-r)*R  # 右側の和
            temp += sum(A[l:r])  # 書き換えなかった部分の和
            ans = min(ans, temp)
    print(ans)


if __name__ == '__main__':
    main()
