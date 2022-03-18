from sys import stdin
from collections import deque

# N: 移動できる回数
# X: 最初にいる頂点の位置
N, X = map(int, stdin.readline().split())
S = input()
# LまたはRの直後にUがある場合、元の頂点に戻る。そのような組み合わせを取り除いたものを以下の dq に格納する
dq = deque()

for s in S:
    if len(dq) > 0:
        popped = dq.pop()
        if (popped == "L" or popped == "R") and s == "U":
            continue
        else:
            dq.append(popped)
            dq.append(s)
    else:
        dq.append(s)

for query in dq:
    if query == "U":
        X //= 2
    elif query == "L":
        X *= 2
    else:
        X = X*2 + 1

print(X)
