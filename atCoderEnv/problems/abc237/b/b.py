#!/usr/bin python
# H, W = map(int, input().split())
# matrix = []
# for _ in range(H):
#     matrix.append(input().split())

# for i in range(W):
#     row = []
#     for vector in matrix:
#         row.append(vector[i])
#     print(" ".join(row))


# 以下、リスト内包と、listの*を用いた出力を使ってコードをもっと短くする
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

print(list(map(list, zip([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]))))
At = list(zip(*A))

for row in At:
    print(*row)

