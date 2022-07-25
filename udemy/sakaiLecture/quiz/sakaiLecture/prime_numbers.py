# 与えられた数字に含まれる全ての素数を含む配列を返す
# Input: 50 => output : [2,3,4,5,11,13,17,19,23,29,31,41,43,47]
from typing import Generator, List
import math


def generate_primes_myans(number: int) -> List[int]:
    primes = []
    for i in range(2, number+1):
        flg = True
        for num in primes:
            if i % num == 0:
                flg = False
                break
        if flg:
            primes.append(i)
    return primes

# 上の実装はfor-else構文を用いるとflg変数を使わなくても済む


def generate_primes_v1(number: int) -> List[int]:
    primes = []
    for x in range(2, number + 1):
        for y in primes:
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes


# 倍数が素数でないことを利用してcacheを使いながら効率化した解法
def generate_primes_v2(number: int) -> List[int]:
    primes = []
    cache = {}
    for x in range(2, number+1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        primes.append(x)
        # 判定した素数の倍数を非素数としてcacheに格納する
        # (その素数の2倍から、指定された数の大きさまで、その素数ステップス進んだ数の配列をrange(x+x, number + 1, x)によって生成している)
        for y in range(x+x, number + 1, x):
            cache[y] = False
    return primes


# Generatorを用いた実装(少し早くなる)
def generate_primes_v3(number: int) -> Generator[int, None, None]:
    cache = {}
    for x in range(2, number+1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        yield x
        # 判定した素数の倍数を非素数としてcacheに格納する
        # (その素数の2倍から、指定された数の大きさまで、その素数ステップス進んだ数の配列をrange(x+x, number + 1, x)によって生成している)
        for y in range(x+x, number + 1, x):
            cache[y] = False


# input [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16...]

def is_prime_myans(number: int) -> bool:
    for prime in generate_primes_v3(number-1):
        if number % prime == 0:
            return False
    else:
        return True


def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


"""
計算コストを上げたもの 素数判定する場合は、その数の平方根までの数しか割り算チェックしなくて良いことを利用した実装
ex)
36 = 2 * 18
36 = 3 * 12
36 = 4 * 9
36 = 6 * 6
これ以降は上の組み合わせの逆verしか見つからない => 素数判定は平方根までチェックするだけで十分とわかる
"""


def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False

    # for i in range(2, math.floor(math.sqrt(num) + 1)):
    #     if num % i == 0:
    #         return False
    # mathライブラリの仕様が禁止された場合は以下のコードに変更する
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


# 偶数を最初に取り除いてさらに計算効率を高める
def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2:
        return False

    for i in range(3, math.floor(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False

    # mathライブラリの仕様が禁止された場合は以下のコードに変更する
    # i = 3
    # while i * i <= num:
    #     if num % i == 0:
    #         return False
    #     i += 2

    return True


if __name__ == "__main__":
    print(generate_primes_v2(50))

    print([i for i in generate_primes_v3(50)])

    print(is_prime_v3(72))
