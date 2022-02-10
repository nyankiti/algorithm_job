# queueよりdequeu使った方が圧倒的に早い！！
from collections import deque
import sys

n = int(input())

deq = deque()


# input()で標準入力を受け取るとTLEしたが、stdinを用いるとうまくいった。。。。
for s in sys.stdin:
    query = s.split()

    if query[0] == "insert":
        data = int(query[1])
        deq.appendleft(data)
    elif query[0] == "deleteFirst":
        deq.popleft()
    elif query[0] == "deleteLast":
        deq.pop()
    else:
        data = int(query[1])
        try:
            deq.remove(data)
        except ValueError:
            continue

print(*deq)
