from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    H, W = map(int, stdin.readline().split())
    factorials = [1, 1]
    for i in range(2, 200001):
        factorials.append((factorials[-1]*i) % MOD)

    bunsi = factorials[H+W-2]
    bunbo = (factorials[H-1]*factorials[W-1]) % MOD

    ans = (bunsi * pow(bunbo, MOD-2, MOD)) % MOD
    print(ans)


if __name__ == '__main__':
    main()
