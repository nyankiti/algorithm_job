# 偶奇に注目する問題。
from sys import stdin

N, K = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())
*B, = map(int, stdin.readline().split())

*each_diff, = map(lambda x: abs(x[0] - x[1]), zip(A, B))
# print(each_diff)


# そもそも偶奇が合わなければ答えが合わない
each_diff_sum = sum(each_diff)
if each_diff_sum % 2 == K % 2:
    K -= each_diff_sum
    # each_diff_sumを引いたKが0以上であれば条件に合う。かつ、残った計算回数が偶数ならば調整できる
    if K >= 0 and K % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
