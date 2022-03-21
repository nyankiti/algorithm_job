from sys import stdin, exit
from operator import mul
from functools import reduce


# r が 2であることが確定しているので、このわざわざコンビネーションを計算するメソッドは必要ない
# def cmb(n, r):
#     r = min(n-r, r)
#     if r == 0:
#         return 1
#     over = reduce(mul, range(n, n - r, -1))
#     under = reduce(mul, range(1, r + 1))
#     return over // under


# _nC_2のコンビネーションを計算するメソッド
def cmb_2(n):
    return n * (n-1) // 2


N = int(stdin.readline())
S = input()

# 連続した要素の数を数える
consecutive_count_list = []
consecutive_count = 1
prev_char = ""
for char in S:
    if char == prev_char:
        consecutive_count += 1
    else:
        prev_char = char
        if consecutive_count >= 2:
            consecutive_count_list.append(consecutive_count)
        consecutive_count = 1
# 最後に連続した数を数える
if consecutive_count >= 2:
    consecutive_count_list.append(consecutive_count)

ans = cmb_2(N)
for count in consecutive_count_list:
    ans = ans - cmb_2(count)

print(ans)
