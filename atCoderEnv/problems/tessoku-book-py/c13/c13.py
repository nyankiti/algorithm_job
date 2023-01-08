from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    N, P = map(int, stdin.readline().split())
    *A, = map(lambda x: int(x) % MOD, stdin.readline().split())
    mod_A_counter = defaultdict(int)

    ans = 0

    for i, a in enumerate(A):
        if a == 0:
            if P == 0:
                ans += i
        else:
            # MOD を法として、P を a で割った値が b となる
            b = P * pow(a, MOD-2, mod=MOD) % MOD
            # print(P, (a*b) % MOD, a, b, mod_A_counter[b])
            ans += mod_A_counter[b]

        # for文の最中にカウントを増やすことで、重複することがなくなる！
        mod_A_counter[a] += 1

    print(ans)


if __name__ == '__main__':
    main()
