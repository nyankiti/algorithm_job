from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    lookpu = {}

    def rec(mass, score):
        if (mass, score) in lookpu:
            return lookpu[(mass, score)]
        if mass == N:
            return score
        else:
            lookpu[(mass, score)] = max(
                rec(A[mass-1], score+100), rec(B[mass-1], score+150))
            return lookpu[(mass, score)]
    print(rec(1, 0))

    # 配る方法が不確定(どのマスから遷移する可能性があるかはわからない)なので、送るDPをする

    # next_mas = 1
    # while next_mas != N:
    #     # 選択肢は以下の二つ
    #     next_mas = A[next_mas-1]
    #     next_mas = B[next_mas-1]


if __name__ == '__main__':
    main()
