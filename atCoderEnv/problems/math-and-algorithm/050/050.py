from sys import stdin

MOD = 1000000007


# 繰り返し二乗法
def pow_original(x, n, mod):
    if n == 0:
        return 1
    if n == 1:
        return x % mod

    if n % 2 == 1:
        return x * pow_original(x, n - 1, mod) % mod
    else:
        t = pow_original(x, n // 2, mod)
        return t * t % mod


def main():
    a, b = map(int, stdin.readline().split())
    # print(pow(a, b, mod=MOD))
    print(pow_original(a, b, mod=MOD))


if __name__ == '__main__':
    main()
