from sys import stdin
# 部分和問題
N, X = map(int, stdin.readline().split())
ab = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp = [[0]*N, [0],N]
print(dp)

def recursive_search(i, sum, target):
    # 終了条件
    if i == N:
        if sum == target:
            return True
        else:
            return False

    # aを選ぶ選択をした場合
    if recursive_search(i+1, sum + ab[i][0], target):
        return True

    # bを選ぶ選択をした場合
    if recursive_search(i+1, sum + ab[i][1], target):
        return True

    return False

if recursive_search(0, 0, X):
    print("Yes")
else:
    print("No")