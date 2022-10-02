from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    # 偶数個の山で、石の数が同じ時は、モノマネ戦略によって Second が勝つ。
    xor_sum = A[0]
    for i in range(1, N):
        xor_sum = xor_sum ^ A[i]

    print("First" if xor_sum != 0 else "Second")


if __name__ == '__main__':
    main()
