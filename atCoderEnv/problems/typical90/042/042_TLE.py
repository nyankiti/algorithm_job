from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
MOD = 10**9 + 7


def main():
    K = int(stdin.readline())

    """
    数字の和がKであるので、答えは大きくとも K桁 であることがわかる。
    """
    ans = 0
    i = 1
    while True:
        num = 9*i
        digit_sum = sum(map(int, str(num)))
        if digit_sum == K:
            ans += 1
            ans %= MOD
        i += 1

        if len(str(num)) > K:
            break
    print(ans % MOD)


if __name__ == '__main__':
    main()
