from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

HASH_MOD = 10000009


def main():
    N, Q = map(int, stdin.readline().split())

    Power_100 = [1]
    for i in range(1, N+1):
        Power_100.append(Power_100[-1]*100 % HASH_MOD)

    S = input()
    Hash_table = [0]
    for i in range(N):
        Hash_table.append((100*Hash_table[-1] + ord(S[i])) % HASH_MOD)

    for _ in range(Q):
        a, b, c, d = map(int, stdin.readline().split())
        left_operand = Hash_table[b] - \
            (Hash_table[a-1]*Power_100[b-a+1]) % HASH_MOD
        left_operand += HASH_MOD
        left_operand %= HASH_MOD

        rigth_operand = Hash_table[d] - \
            (Hash_table[c-1]*Power_100[d-c+1]) % HASH_MOD
        rigth_operand += HASH_MOD
        rigth_operand %= HASH_MOD

        # print(left_operand, rigth_operand)
        if left_operand == rigth_operand:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
