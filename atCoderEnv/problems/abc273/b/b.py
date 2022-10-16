import math
from sys import stdin, setrecursionlimit
from decimal import Decimal, ROUND_HALF_UP
setrecursionlimit(10**6)


def main():
    X, K = map(int, stdin.readline().split())

    for i in range(K):
        X = X/(10**(i+1))
        # print(X)
        X = Decimal(str(X)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
        X *= (10**(i+1))
        # print(X)
    print(X)


if __name__ == '__main__':
    main()
