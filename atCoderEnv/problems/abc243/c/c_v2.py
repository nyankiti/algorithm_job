from sys import stdin, exit

N = int(stdin.readline())
people_coordinates = []

for _ in range(N):
    people_coordinates.append(list(map(int, stdin.readline().split())))

S = input()

# 同じ高さ(yの値)をもつ点とその方向を管理するdict
# [(x軸の値, 進方向), (x軸の値, 進方向), ...] と値を持たせる
same_rows = {}

for index, direction in enumerate(S):
    person = people_coordinates[index]
    height = person[1]
    # same_rows.get(height, []).append((person[0], direction))
    row = same_rows.get(height)

    if row:
        same_rows[height].append((person[0], direction))
    else:
        # 同じ高さに人がいない場合
        same_rows[height] = [(person[0], direction)]

for height in same_rows:
    row = same_rows[height]
    row.sort(key=lambda x: x[0])

    is_rifht_direction_exit = False
    for in_row_persion in row:
        if is_rifht_direction_exit and in_row_persion[1] == "L":
            print("Yes")
            exit()
        elif in_row_persion[1] == "R":
            is_rifht_direction_exit = True

print("No")


# こちらがACされた！！
