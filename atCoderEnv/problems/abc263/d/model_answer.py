import math
from sys import stdin


def main():
    N, L, R = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # 累積和を計算 accumulate[i] = A[0] + A[1] + ... + A[i-1]
    accumulate = [0]
    for a in A:
        accumulate.append(accumulate[-1] + a)

    # left[l] = l * L - accumulate[l]
    left = [l * L - accumulate[l] for l in range(N+1)]

    # right[r] = (N-r)*R+accumulate[r]
    right = [(N - r) * R + accumulate[r] for r in range(N+1)]

    ans = math.inf

    # 全探索
    # for l in range(N+1):
    #     for r in range(l, N+1):
    #         # temp = l*L  # 左側の和
    #         # temp += (N-r)*R  # 右側の和
    #         # temp += (accumulate[r] - accumulate[l])  # 書き換えなかった部分の和

    #         # 上の3行を l に関する部分と r に関する部分に分離する
    #         # temp = (l*L - accumulate[l]) + ((N-r)*R+accumulate[r])

    #         # 分離したのもは、left, rightに累積和の応用のように前計算しておいておくことができる
    #         temp = left[l] + right[r]
    #         ans = min(ans, temp)

    # 上の temp = left[l] + right[r] を応用してさらに最適化する

    # 最小値をとる累積和
    rightmin = right
    for i in range(N-1, -1, -1):
        rightmin[i] = min(rightmin[i], rightmin[i+1])

    for l in range(N+1):
        # temp = left[l] + min(right[l:]) <= min(right[l:] の部分をrightminにて前計算しておくと良い！！)
        # ans = min(ans, temp)
        temp = left[l] + rightmin[l]
        ans = min(ans, temp)

    print(ans)


if __name__ == '__main__':
    main()
