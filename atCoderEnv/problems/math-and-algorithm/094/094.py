import math
from sys import stdin


def main():
    N = int(stdin.readline())
    *B, = map(int, stdin.readline().split())
    A = [math.inf]*N

    for i, b in enumerate(B):
        A[i] = min(b, A[i])
        A[i+1] = min(b, A[i+1])

    print(sum(A))


if __name__ == '__main__':
    main()
