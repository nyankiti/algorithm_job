from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


HASH_MOD = 1000000007


def main():
    N, Q = map(int, stdin.readline().split())

    Power_100 = [1]
    for i in range(1, N+1):
        Power_100.append(Power_100[-1]*100 % HASH_MOD)

    S = input()
    Hash_table = [0]
    Hash_table_rev = [0]
    for i in range(N):
        Hash_table.append((100*Hash_table[-1] + ord(S[i])) % HASH_MOD)
    for i in range(N-1, -1, -1):
        Hash_table_rev.append((100*Hash_table_rev[-1] + ord(S[i])) % HASH_MOD)

    for _ in range(Q):
        l, r = map(int, stdin.readline().split())
        jun = Hash_table[r] - (Hash_table[l-1]*Power_100[r-l+1]) % HASH_MOD
        jun %= HASH_MOD
        gyaku = Hash_table_rev[N-l+1] - \
            (Hash_table_rev[N-r]*Power_100[r-l+1]) % HASH_MOD
        gyaku %= HASH_MOD
        if jun == gyaku:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
