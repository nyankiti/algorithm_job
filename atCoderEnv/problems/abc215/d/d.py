from sys import stdin


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

    ans_li = [True]*(M+1)
    for factor in factors.keys():
        for i in range(factor, M+1, factor):
            ans_li[i] = False

    # 0を取り除く
    ans_li[0] = False

    print(ans_li.count(True))
    for index, val in enumerate(ans_li):
        if val:
            print(index)


if __name__ == '__main__':
    main()
