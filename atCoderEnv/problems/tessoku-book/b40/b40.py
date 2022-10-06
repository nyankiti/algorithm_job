from collections import Counter, defaultdict
import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(lambda x: int(x) % 100, stdin.readline().split())
    c = Counter(A)
    ans = 0
    for i in range(1, 50):
        ans += (c[i] * c[100-i])
    # 50と0の分
    ans += math.comb(c[50], 2)
    ans += math.comb(c[0], 2)
    print(ans)


if __name__ == '__main__':
    main()
