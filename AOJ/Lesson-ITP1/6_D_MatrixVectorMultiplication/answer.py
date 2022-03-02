from sys import stdin

n, m = map(int, stdin.readline().split())
matrix = []
vector = []

for _ in range(n):
    *row, = map(int, stdin.readline().split())
    matrix.append(row)

for _ in range(m):
    vector.append(int(stdin.readline()))

for row in matrix:
    result = 0
    for i, j in zip(row, vector):
        result += i*j
    print(result)