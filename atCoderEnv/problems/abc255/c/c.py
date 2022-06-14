import math
from sys import stdin
import bisect
"""
等差数列の一般公
A_n = A + (N-1)*D
 
Xに最も近いA_nを探せばよい
 
=> Dで割ってある程度範囲を絞った数列を作って二分探索する
"""


def main():
    X, A, D, N = map(int, stdin.readline().split())
    A_n = []

    if D == 0:
        print(abs(A-X))
    if D > 0:
        # 末項
        A_max = A + (N-1)*D
        # 初項
        A_min = A
        if X <= A_min:
            print(abs(A_min - X))
        elif X >= A_max:
            print(abs(A_max - X))
        else:
            B = (X-A)//D
            for i in range(max(B-80, 0), min(B+80, N+1)):
                A_n.append(A + i*D)

            left_index = bisect.bisect_left(A_n, X)
            ans = math.inf
            for i in range(max(left_index-100, 1), min(left_index+100, len(A_n))):
                ans = min(ans, abs(A_n[i]-X))
            print(ans)

    elif D < 0:
        # 公差が負の時
        # 末項
        A_min = A + (N-1)*D
        # 初項
        A_max = A
        if X <= A_min:
            print(abs(A_min - X))
        elif X >= A_max:
            print(abs(A_max - X))
        else:
            B = (X-A)//D
            for i in range(max(B-80, 0), min(B+80, N+1)):
                A_n.append(A + i*D)

            left_index = bisect.bisect_left(A_n, X)
            ans = math.inf
            for i in range(max(left_index-100, 1), min(left_index+100, len(A_n))):
                ans = min(ans, abs(A_n[i]-X))
            print(ans)


if __name__ == '__main__':
    main()
