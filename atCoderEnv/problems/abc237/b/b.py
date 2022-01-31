#!/usr/bin python
H, W = map(int, input().split())
matrix = []
for _ in range(H):
    matrix.append(input().split())

for i in range(W):
    row = []
    for vector in matrix:
        row.append(vector[i])
    print(" ".join(row))

