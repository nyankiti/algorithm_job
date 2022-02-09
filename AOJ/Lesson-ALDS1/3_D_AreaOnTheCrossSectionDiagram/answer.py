# queueよりdequeu使った方が圧倒的に早い！！
from collections import deque
from typing import Deque


def calclateArea(deq: Deque):
    if len(deq) == 1:
        deq.pop()
        return 0
    if deq[0] == "\\" and deq[len(deq)-1] == "/":
        space = len(deq) - 2
        deq.pop()
        deq.popleft()
        return space + 1
    else:
        if deq[0] != "\\":
            deq.popleft()
            calclateArea(deq)
        elif deq[len(deq)-1] != "/":
            deq.pop()
            calclateArea(deq)


terrain = input()

deq = deque()
result = []

for elem in terrain:
    # まず、deqに要素が既に入っているかどうかで大きく挙動が異なる
    if deq:
        deq.append(elem)
        # "/" がきた場合は、既にある "\" の数を数えて谷が形成されるかどうかを判定する必要がある
        if deq.count("\\") == deq.count("/"):
            # 谷が形成された場合、その谷にどれだけ水が貯まるのかを算出する
            area = 0
            while deq:
                area += calclateArea(deq)
            result.append(area)
    else:
        # if elem == "\\":
        deq.append(elem)
        # else:
        #     # deqが空の状態で "_","/" は水たまりを作らないので無視する
        #     continue


print(sum(result))
print(len(result), *result)
