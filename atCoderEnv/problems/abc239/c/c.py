from sys import stdin, exit
import math

x_1, y_1, x_2, y_2 = map(int, stdin.readline().split())

# 平行移動
x_2 = x_2 - x_1
y_2 = y_2 - y_1
y_1 = 0
x_1 = 0
# # 二つの円の交点を求める
c = (x_2**2 + y_2**2)/2

for x in range(-3, 3):
    for y in range(-3, 3):
        if x*x_2 + y*y_2 - c == 0:
            if x_2 == 2 and y_2 == 2:
                continue
            print("Yes")
            exit()

print("No")

# if x_1 < x_2:
#     x_start = x_1 - 3
#     x_end = x_2 + 3
# else:
#     x_start = x_2 - 3
#     x_end = x_1 + 3

# if y_1 < y_2:
#     y_start = y_1 - 3
#     y_end = y_2 + 3
# else:
#     y_start = y_2 - 3
#     y_end = y_1 + 3

# for x in range(x_start, x_end):
#     for y in range(y_start, y_end):
#         x = 10**9+1
#         y = 10**9-2
#         if x*a + y*b - c == 0.0:
#             print("Yes")
#             exit()

# print("No")