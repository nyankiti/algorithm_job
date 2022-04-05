import numpy as np
# 多項式の計算はnumpyが勝手にやってくれる


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))[::-1]
    C = list(map(int, input().split()))[::-1]
    A_poly = np.poly1d(A)
    C_poly = np.poly1d(C)
    B = C_poly / A_poly
    print(*map(int, reversed(B[0].c)))


if __name__ == '__main__':
    main()
