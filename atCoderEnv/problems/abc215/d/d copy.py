from sys import stdin
import math


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # Aに出てくる約数を全てかけた倍数を作る
    factors = {}

    def factorization(n):
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp % i == 0:
                factors[i] = True
                while temp % i == 0:
                    temp //= i
        if temp != 1:
            factors[temp] = True

    for a in A:
        factorization(a)

    # # print(factors)

    # A_factors_product = 1
    # for factor in factors.keys():
    #     A_factors_product *= factor

    # Mまでの素数を列挙して、A_factor_productの因数になっていないものが答え
    ans = {1: True}
    for i, val in enumerate(sieve_of_eratosthenes(M)):
        if val:
            if i not in factors:
                for j in range(i, M+1, i):
                    ans[j] = True

    ans_li = list(ans.keys())
    ans_li.sort()
    print(len(ans_li))
    for num in ans_li:
        print(num)


if __name__ == '__main__':
    main()
