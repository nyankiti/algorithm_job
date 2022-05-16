from sys import stdin, exit


def main():
    N, W = map(int, stdin.readline().split())
    # N == 1, N == 2 の場合を調べるのが面倒なので、0を二つ足しておくことで対応する
    A = list(map(int, stdin.readline().split())) + [0, 0]

    di = {}
    for i in range(N + 2):
        for j in range(i):
            for k in range(j):
                temp_sum = A[i] + A[j] + A[k]
                if temp_sum <= W:
                    di[temp_sum] = True
    print(len(di.keys()))


if __name__ == '__main__':
    main()
