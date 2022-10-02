import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    n, r = map(int, stdin.readline().split())
    factorials = [1, 1]
    for i in range(2, 100001):
        factorials.append((factorials[-1]*i) % MOD)

    bunsi = factorials[n]
    bunbo = (factorials[r]*factorials[n-r]) % MOD

    ans = (bunsi * pow(bunbo, MOD-2, MOD)) % MOD
    print(ans)


if __name__ == '__main__':
    main()
