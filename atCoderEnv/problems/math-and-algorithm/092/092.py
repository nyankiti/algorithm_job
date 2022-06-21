import math
from sys import stdin


def main():
    N = int(stdin.readline())

    ans = math.inf
    for i in range(1, math.ceil(math.sqrt(N))+1):
        if N % i == 0:
            ans = min(ans, i+N//i)

    print(ans*2)


if __name__ == '__main__':
    main()
