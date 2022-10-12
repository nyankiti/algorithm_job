from collections import Counter
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    A = [int(stdin.readline()) for _ in range(N)]
    c = Counter(A)
    ans = 0
    for key in c.keys():
        if c[key] > 1:
            ans += (c[key]-1)*c[key]//2
    print(ans)


if __name__ == '__main__':
    main()
