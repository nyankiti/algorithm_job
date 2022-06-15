from sys import stdin
MOD = 1000000007


# 逆元を使って割り算を処理するとなぜかWAしてしまう、、、
# def main():
#     N = int(stdin.readline())
#     *A, = map(int, stdin.readline().split())

#     fact = [1]*N
#     for i in range(1, N):
#         fact[i] = i*fact[i-1] % MOD

#     def division(a, b):
#         return (a * pow(b, MOD-2, mod=MOD)) % MOD

#     def nCr(n, r):
#         return division(fact[n], fact[r]*fact[n-r] % MOD)

#     ans = 0
#     for i in range(N):
#         ans += nCr(N-1, i)*A[i]
#     print(ans)


# if __name__ == '__main__':
#     main()


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    fact = [1]
    for i in range(1, N + 1):
        fact.append((fact[-1] * i) % MOD)

    def combination(m, k):
        return (fact[m] * pow(fact[k], -1, MOD) * pow(fact[m - k], -1, MOD)) % MOD

    ans = 0
    for i in range(N):
        ans = (ans + A[i] * combination(N - 1, i)) % MOD
    print(ans)


if __name__ == '__main__':
    main()
