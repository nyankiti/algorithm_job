from collections import Counter
import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    c = Counter(A)
    ans = 0
    for key in c.keys():
        if c[key] >= 3:
            # print(math.comb(c[key], 3))
            ans += math.comb(c[key], 3)
    print(ans)


if __name__ == '__main__':
    main()
