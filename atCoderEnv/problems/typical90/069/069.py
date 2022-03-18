from re import X
from sys import stdin, exit

mod = 10**9+7

# オリジナルの繰り返しニ乗法

N, K = map(int, stdin.readline().split())

# corner case
if N == 1:
    print(K)
    exit()
if K == 1:
    print(0)
    exit()

# オリジナルの繰り返しニ乗法


def pow_original(x, n):
    ans = 1
    while n:
        if n % 2:
            ans = ans * x % mod
        x = x * x % mod
        # n >>= 1
        # 右のビットシフトは以下のように2で割った整数部を求める操作と等しい
        n //= 2
    return ans


# ans = K*(K-1) * pow(K-2, N-2, mod=mod) % mod
ans = K*(K-1) * pow_original(K-2, N-2) % mod
print(ans)
