from sys import stdin

# N: 移動できる回数
# X: 最初にいる頂点の位置
N, X = map(int, stdin.readline().split())
S = input()


def parent_index(index: int):
    return index // 2


def left_child_index(index: int):
    return 2 * index


def right_child_index(index: int):
    return 2 * index + 1


for query in S:
    if query == "U":
        X = parent_index(X)
    elif query == "L":
        X = left_child_index(X)
    else:
        X = right_child_index(X)

print(X)
