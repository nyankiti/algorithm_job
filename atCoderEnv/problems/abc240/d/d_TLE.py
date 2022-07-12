from sys import stdin
from collections import deque

deq = deque()
n = int(stdin.readline())
*A, = map(int, stdin.readline().split())


def revive_memo(deq, memo):
    if len(deq) == 0:
        return

    poped = deq.pop()
    deq.append(poped)

    count = 1
    for i in range(1, len(deq)):
        if deq[i-1] == deq[i]:
            count += 1
        else:
            count = 1
    for i in range(count):
        memo.append(poped)




deq.append(A[0])
memo = [A[0]]

print(len(deq))

for a in A[1:]:
    poped = deq.pop()
    deq.append(poped)
    deq.append(a)

    if a == poped:
        memo.append(a)
        # 次に入れる数が直前の数と一致した場合
        if a == len(memo):
            # memoの分だけdeqの中身が消える
            for i in range(len(memo)):
                deq.pop()
            # 中身を消した後、memoを消した直前の数字のものに復活させる
            memo.clear()
            revive_memo(deq, memo)

    else:
        # 連続が終了するので、memoをクリアする
        memo.clear()
        memo.append(a)

    print(len(deq))
