from sys import stdin


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return set(a)


def main():
    N, K = map(int, stdin.readline().split())
    *V, = map(int, stdin.readline().split())
    V.sort()
    # Vを素数だけにする
    temp_set = set()
    for v in V:
        factors = prime_factorize(v)
        for factor in factors:
            if factor in temp_set:
                break
        else:
            temp_set.add(v)

    prime_V = list(temp_set)
    print(prime_V)
    K = len(prime_V)

    yojishou = 0
    for i in range(2 ** K):
        temp_multiple = 1
        parity = 0
        for j in range(K):
            if ((i >> j) & 1):
                parity += 1
                temp_multiple *= prime_V[j]
        if parity % 2 == 0:
            # print("-", parity,  temp_multiple, N//temp_multiple)
            yojishou -= (N//temp_multiple)
        else:
            # print("+", parity, temp_multiple, N//temp_multiple)
            yojishou += (N//temp_multiple)

    # print("^-------------------^")

    yojishou += N

    print(yojishou)


if __name__ == '__main__':
    main()
