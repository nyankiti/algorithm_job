from sys import stdin, exit


def detect_collision(x_1, x_1_direction, x_2, x_2_direction):
    if x_1 > x_2 and x_1_direction == "L" and x_2_direction == "R":
        return True
    elif x_1 < x_2 and x_1_direction == "R" and x_2_direction == "L":
        return True
    else:
        return False


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

    row = same_rows.get(height)

    if row:
        # 既に同じ高さに人がいる場合
        for in_row_persion in same_rows[height]:
            if detect_collision(in_row_persion[0], in_row_persion[1], person[0], direction):
                print("Yes")
                exit()
        else:
            same_rows[height].append((person[0], direction))
    else:
        # 同じ高さに人がいない場合
        same_rows[height] = [(person[0], direction)]

print("No")
