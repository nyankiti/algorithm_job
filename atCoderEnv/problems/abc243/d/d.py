from sys import stdin

# N: 移動できる回数
# X: 最初にいる頂点の位置
N, X = map(int, stdin.readline().split())
S = input()

for query in S:
    if query == "U":
        X //= 2
    elif query == "L":
        X *= 2
    else:
        X = X*2 + 1

print(X)
