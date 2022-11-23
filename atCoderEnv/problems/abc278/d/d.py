from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    Q = int(stdin.readline())
    # 差分が0でない箇所をうまく保持することで計算量を削減する
    sabun = defaultdict(int)
    for i, a in enumerate(A):
        sabun[i] += a

    for _ in range(Q):
        *query, = map(int, stdin.readline().split())
        if query[0] == 1:
            defalt_val = query[1]
            # 一度 defalt_valに代入しておく。出ないと、defauldictは存在しないkeyを指定された時、
            # ポインターをたどって値を生成するので、以下のようにしたらバグる
            # sabun = defaultdict(lambda: query[1])
            sabun = defaultdict(lambda: defalt_val)
            sabun["test"] = query[1]
            # print("pure", sabun[0])
        elif query[0] == 2:
            sabun[query[1]-1] = sabun[query[1]-1] + query[2]
        else:
            print(sabun[query[1]-1])


if __name__ == '__main__':
    main()
