# 与えられるSの要素が昇順に並べられていることを利用して、二分探索で解く。

N = int(input())
S = list(map(int, input().split()))

DICT = {}

for i in range(N):
    DICT[S[i]] = True

Q = int(input())
T = list(map(int, input().split()))

ans = 0

for i in range(Q):
    # hash tableの要素の参照の計算量はO(log(N))であるので、探索の効率が上がる
    # if DICT.__contains__(T[i]):
    if T[i] in DICT:
        ans += 1

print("%d" % (ans))
