from sys import stdin

n = int(stdin.readline())

chessboard = [["."]*8 for _ in range(8)]

# 指定のクイーンが通れる範囲を全て潰すメソッド


def queen_traversal(chessboard, r, c):
    for i in range(8):
        if chessboard[r][i] == ".":
            chessboard[r][i] = "#"

    for i in range(8):
        if chessboard[i][c] == ".":
            chessboard[i][c] = "#"

    # 右斜め上
    i = 1
    while r + i <= 7 and c - i >= 0:
        if chessboard[r + i][c - i] == ".":
            chessboard[r + i][c - i] = "#"
        i += 1
    # 左斜め上
    i = 1
    while r - i >= 0 and c - i >= 0:
        if chessboard[r - i][c - i] == ".":
            chessboard[r - i][c - i] = "#"
        i += 1
    # 右斜め下
    i = 1
    while r + i <= 7 and c + i <= 7:
        if chessboard[r + i][c + i] == ".":
            chessboard[r + i][c + i] = "#"
        i += 1
    # 左斜め下
    i = 1
    while r - i >= 0 and c + i <= 7:
        if chessboard[r - i][c + i] == ".":
            chessboard[r - i][c + i] = "#"
        i += 1


queen_count = 0
for _ in range(n):
    r, c = map(int, stdin.readline().split())
    chessboard[r][c] = "Q"
    queen_traversal(chessboard, r, c)
    queen_count += 1


for i in range(8):
    for j in range(8):
        if chessboard[i][j] == ".":
            chessboard[i][j] = "Q"
            queen_traversal(chessboard, i, j)

for row in chessboard:
    print(row)
