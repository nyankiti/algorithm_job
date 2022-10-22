from sys import stdin, setrecursionlimit
from decimal import Decimal, ROUND_HALF_UP

setrecursionlimit(10**6)


def main():
    A, B = map(int, stdin.readline().split())
    X = Decimal(str(B/A)).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)
    print(X)


if __name__ == '__main__':
    main()
