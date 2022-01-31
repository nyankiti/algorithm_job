#!/usr/bin python
S = input()

# if S == S[-1::-1]:
#     print("Yes")


# 任意の個数の後ろのaを再起的に数える
def count_back_a(S: str, count: int):
    if S and S[-1] == "a":
        # 1番後ろの文字を取り除く
        _S = S[:-1]
        count += 1
        return count_back_a(_S, count)
    else:
        return count

a_count = count_back_a(S, 0)

new_S = ("a" * a_count) + S

if new_S == new_S[::-1]:
    print("Yes")
else:
    print("No")

# for i in range(a_count+1):
#     temp = ("a" * i)+S
#     # 回文ができているかチェック
#     if temp == temp[::-1]:
#         print("Yes")
#         break
# else:
#     print("No")