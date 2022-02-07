import math

# 素数判定では「合成数xはp≤√xを満たす素因子pをもつ」という性質を利用することができる。 => √xまでしか探索しなくて良い！
pow


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(x) + 1)):
        if x % i == 0:
            return False

    return True


# 偶数を最初に取り除いてさらに計算効率を高める
def is_prime_v2(x) -> bool:
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2:
        return False

    for i in range(3, math.floor(math.sqrt(x) + 1), 2):
        if x % i == 0:
            return False

    # mathライブラリの仕様が禁止された場合は以下のコードに変更する
    # i = 3
    # while i * i <= num:
    #     if num % i == 0:
    #         return False
    #     i += 2

    return True


# Fermat's little theorem
def is_prime_v3(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        return 2**(x-1) % x == 1
        # return pow(2, x - 1, x) == 1


N = int(input())

result = 0

for _ in range(N):
    num = int(input())
    if is_prime_v3(num):
        result += 1


print(result)
