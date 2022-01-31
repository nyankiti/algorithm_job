# 以下の回答でも7個ほどruntime errorとなってしまう。テストケースが公開されたらまた考えよう
import sys

S = input()
len_S = len(S)

# 先頭のaの数を数える
x = 0
for i in range(len_S):
    if S[i] == "a":
        x += 1
    else:
        break

# 後ろのxの数を数える
y = 0
for i in range(len_S-1, 0, -1):
    if S[i] == "a":
        y += 1
    else:
        break

if x == len_S:
    print("Yes")
elif x > y:
    print("No")
else:
    for i in range(0, x-y):
        if S == S[-1::-1]:
            print("Yes")
    else:
        print("Yes")
