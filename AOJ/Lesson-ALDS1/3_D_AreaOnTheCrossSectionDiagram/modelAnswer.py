# \と/を別々のスタックで管理していくのがポイント！！
# 自分のanswerでは全てを一つのスタックで管理しようとしていた。そもそもの発想が間違っていたことに気付くのが遅かった。。。。

from collections import deque

stack1 = deque()  # \の位置を積んでいくスタック
stack2 = deque()  # 各々の水たまりの面積を[一番左の/の位置、その水たまりの面積]の形で積んでいくスタック
all_area = 0  # 総面積

terrain = list(input())

# for i in range(len(st)):  # 実際に一文字ずつ読み取って総面積計算
for i, elem in enumerate(terrain):
    if elem == '\\':
        stack1.append(i)
    elif elem == '/' and len(stack1) != 0:
        left = stack1.pop()
        all_area += i - left
        area = 0
        while len(stack2) != 0 and left < stack2[-1][0]:
            area += stack2.pop()[1]
        stack2.append([left, area + i - left])

print(all_area)
print(str(len(stack2)), *[i[1] for i in stack2])
