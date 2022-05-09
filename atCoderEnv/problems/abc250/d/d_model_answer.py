from sys import stdin


# 素数表を作成する
def make_prime_list(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            # 素数の場合、その倍数を全て合成数として素数表を更新する
            for j in range(i*2, n+1, i):
                is_prime[j] = False

    return [i for i in range(n+1) if is_prime[i]]


def main():
    N = int(stdin.readline())

    # N = 10^18でqは素数の3錠であるので、10^6までの素数表を調べれば良い。
    prime_list = make_prime_list(10**6)

    ans = 0

    Q = len(prime_list)
    for i in range(Q):
        p = prime_list[i]
        for j in range(i+1, Q):
            q = prime_list[j]
            if N < p*q*q*q:
                break
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
