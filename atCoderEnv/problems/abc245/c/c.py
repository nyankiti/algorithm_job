from sys import stdin, exit
from typing import List
import gc

N, K = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())
*B, = map(int, stdin.readline().split())

# 問題は両方選べる時 => 複数の分岐を考える必要がある

flg = False


def judge(li: List[int], pos):
    global flg

    if pos == N-1:
        flg = True
        return

    if abs(li[pos-1] - A[pos]) <= K and (abs(A[pos] - A[pos+1]) <= K or abs(A[pos] - B[pos+1]) <= K):
        temp = li[:]
        temp.append(A[pos])
        judge(temp, pos + 1)

    if abs(li[pos-1] - B[pos]) <= K and (abs(B[pos] - A[pos+1]) <= K or abs(B[pos] - B[pos+1]) <= K):
        temp = li[:]
        temp.append(B[pos])
        judge(temp, pos + 1)

    del li
    gc.collect()


X = []
X.append(A[0])
judge(X, 1)

Y = []
Y.append(B[0])
judge(Y, 1)

print("Yes" if flg else "No")
