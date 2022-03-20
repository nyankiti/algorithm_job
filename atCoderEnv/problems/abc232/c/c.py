"""
参考：https://qiita.com/u2dayo/items/6a6f784abed82c317805#c%E5%95%8F%E9%A1%8Cgraph-isomorphism

反省点
問題文の同型である条件に、「Pは (1, 2, ... ,N) を並び替えて得られる」とヒントが書いているので、permutationの全探索を思いつくことができたはず
Nが以下であることにも注目すべきだった

"""

from itertools import permutations
from sys import stdin


N, M = map(int, stdin.readline().split())

G1 = [[False] * N for _ in range(N)]
G2 = [[False] * N for _ in range(N)]

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    G1[A-1][B-1] = True
    G1[B-1][A-1] = True

for _ in range(M):
    C, D = map(int, stdin.readline().split())
    G2[C-1][D-1] = True
    G2[D-1][C-1] = True


def is_same_shape(P):
    for i in range(N):
        for j in range(N):
            if G1[P[i]][P[j]] != G2[i][j]:
                return False
    return True


for perm in permutations(range(N)):
    if is_same_shape(perm):
        print("Yes")
        break
else:
    print("No")
