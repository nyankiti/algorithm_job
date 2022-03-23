# bit全探索 recursive version
from sys import stdin

N, S = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

flg = False


def dfs(position, temp_sum):
    global flg

    if position == N-1:
        if temp_sum == S or temp_sum+A[position] == S:
            flg = True
        return

    # 選ぶ場合
    dfs(position+1, temp_sum+A[position])
    # 選ばない場合
    dfs(position+1, temp_sum)


dfs(0, 0)

print("Yes" if flg else "No")
