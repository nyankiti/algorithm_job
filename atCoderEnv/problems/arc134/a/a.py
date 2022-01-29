#!/usr/bin python
N, L, W = map(int, input().split())
A_arr = list(map(int, input().split()))

result = 0

def add_sheet_count(diff):
    if diff > 0 and diff <= W:
        return 1
    elif diff > W:
        return diff // W
    else:
        return 0

# 最初の隙間
result += add_sheet_count(A_arr[0])

# 数列a_iの探索
for i in range(N-1):
    result += add_sheet_count(A_arr[i+1] - A_arr[i] - W)

# 最後の隙間のチェック
result += add_sheet_count(L - (A_arr[N-1] +W ))

print(result)