"""
ポイント1 
記号を0, 1の数字で扱うことで、連続する数のカウントを容易にする
"#" => 1, "." => 0


ポイント2 
右方向、下方向、左下方向、右下方向 の4方向を全てのマスから探索することで、単純な二重forループで全探索できる


ポイント3
judgeメソッドにて、探索方向も受け取ることで探索のメソッドを共通化している


注意
pypyで提出しなければTLEになる
"""

from sys import stdin, exit

N = int(stdin.readline())

grid = [[1 if c == "#" else 0 for c in input()] for _ in range(N)]

# for row in grid:
#     print(row)


def judge(start_row, start_col, direction_row, direction_col):
    # 始点(start_row, start_col) 移動方向(direction_row, direction_col)
    row, col = start_row, start_col
    count = 0
    for _ in range(6):
        if not (0 <= row < N and 0 <= col < N):  # はみ出し判定
            return False
        count += grid[row][col]
        row += direction_row
        col += direction_col
    return count >= 4


direction_pattern = [(1, 0), (0, 1), (1, -1), (1, 1)]

for row in range(N):
    for col in range(N):
        for direction_row, direction_col in direction_pattern:
            if judge(row, col, direction_row, direction_col):
                print("Yes")
                exit()
print("No")
