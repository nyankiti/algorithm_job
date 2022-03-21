from sys import stdin

H, W = map(int, stdin.readline().split())
A = []
B = []

for _ in range(H):
    *a_row, = map(int, stdin.readline().split())
    A.append(a_row)

for _ in range(H):
    *b_row, = map(int, stdin.readline().split())
    B.append(b_row)

count = 0

for x in range(H-1):
    for y in range(W-1):
        diff = B[x][y] - A[x][y]
        count += abs(diff)
        A[x][y] = A[x][y] + diff
        A[x+1][y] = A[x+1][y] + diff
        A[x][y+1] = A[x][y+1] + diff
        A[x+1][y+1] = A[x+1][y+1] + diff

    if B[x] != A[x]:
        print("No")
        break
else:
    print("Yes")
    print(count)
