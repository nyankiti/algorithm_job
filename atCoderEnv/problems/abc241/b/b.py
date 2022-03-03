from sys import stdin

N, M = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split()) # 家にあるパスタの長さ
*B, = map(int, stdin.readline().split()) # i日目に食べるパスタの長さ


flg = True
for b in B:
    if b in A:
        A.remove(b)
    else:
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")
