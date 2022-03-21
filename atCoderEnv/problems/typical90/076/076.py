"""
円を2倍にすることで列として捉え、累積和を利用する
探索は二分探索を行う
"""

from sys import stdin, exit

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())

all = sum(A)
A_double = A + A

# Bに累積和を格納する
B = [0]
temp_sum = 0
for a in A_double:
    temp_sum += a
    B.append(temp_sum)

# print(B)
len_B = len(B)
for i in range(len_B):
    # 二分探索で幅を効率的に探す
    left_index = i
    right_index = len_B - 1
    while left_index <= right_index:
        j = (left_index + right_index) // 2
        if (B[j] - B[i])*10 == all:
            print("Yes")
            exit()
        elif (B[j] - B[i])*10 > all:
            right_index = j-1
        else:
            left_index = j+1


print("No")
