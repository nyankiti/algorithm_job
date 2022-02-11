from collections import defaultdict


# 重複を数えてはいけないのがポイント
# 解法1:setを使う方法
n = input()
S = set(input().split())
q = input()
T = set(input().split())
print(len(S & T))


# 解法2:hash mapを用いてvisitedを管理する方法
n = int(input())
*S, = map(int, input().split())
q = int(input())
*T, = map(int, input().split())

visited = defaultdict(lambda: False)

for i in range(q):
    for j in range(n):
        if T[i] == S[j]:
            visited[T[i]] = True


print(list(visited.values()).count(True))


# 解法3: hash tableの特徴を利用して計算量O(n)に抑える方法
N = int(input())
S = list(map(int, input().split()))

DICT = {}

for i in range(N):
    DICT[S[i]] = True

Q = int(input())
T = list(map(int, input().split()))

ans = 0

for i in range(Q):
    # hash tableの要素の参照の計算量はO(log(N))であるので、探索の効率が上がる
    # if DICT.__contains__(T[i]):
    if T[i] in DICT:
        ans += 1

print("%d" % (ans))
