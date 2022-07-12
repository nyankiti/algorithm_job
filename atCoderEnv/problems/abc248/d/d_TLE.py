from sys import stdin
from collections import defaultdict
import copy


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    Q = int(stdin.readline())

    # カウンターの階差を作る
    d = defaultdict(int)
    kaisa = [d]
    for a in A:
        temp_d = copy.deepcopy(kaisa[-1])
        temp_d[a] += 1
        kaisa.append(temp_d)

    # for di in kaisa:
    #     print(di)

    for _ in range(Q):
        L, R, X = map(int, stdin.readline().split())
        ans = kaisa[R][X] - kaisa[L-1][X]
        print(ans)


if __name__ == '__main__':
    main()
