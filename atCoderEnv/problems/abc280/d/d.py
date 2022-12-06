from sys import stdin, setrecursionlimit
import math

setrecursionlimit(10**6)

# この問題は単調性があるので二分探索するのが最も簡単な解放！
# 本番中に自分が考えたルジャンドルの定理を使う実装は逆に変態な解放かも?


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    K = int(stdin.readline())

    # # 以下のような場合にWAする
    # K = (3**7)*(5**2)
    # print(K)

    # Kに含まれる最も大きい素数を探
    factors = factorization(K)
    # last_prime = factors[-1][0]
    # last_prime_count = factors[-1][1]
    # print(last_prime, last_prime_count)
    ans_li = []
    for last_prime, last_prime_count in factors:
        if last_prime >= last_prime_count:
            # print(last_prime*last_prime_count)
            ans_li.append(last_prime*last_prime_count)
        else:
            prime_multiple = [last_prime *
                              i for i in range(1, last_prime_count+1)]
            # print(prime_multiple)
            temp_count = 0
            for i, val in enumerate(prime_multiple):
                while val % last_prime == 0:
                    temp_count += 1
                    val //= last_prime
                    if temp_count == last_prime_count:
                        # print(last_prime*(i+1))
                        ans_li.append(last_prime*(i+1))
                        break

    print(max(ans_li))


if __name__ == '__main__':
    main()
