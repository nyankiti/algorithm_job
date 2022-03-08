import math
from sys import stdin
from itertools import permutations


# N <= 10 であるので、全探索ができそう
N = int(stdin.readline())

A = []  # 各選手の区間ごとのタイム
for _ in range(N):
    *row, = map(int, stdin.readline().split())
    A.append(row)


M = int(stdin.readline())

bad_relations = []
for _ in range(M):
    x, y = map(int, stdin.readline().split())
    bad_relations.append(tuple((x-1, y-1)))


# bad_relationsを気にせずに駅伝を終了するための最小値を探索する
min_time = math.inf

for perm in permutations([i for i in range(N)]):
    temp = 0
    prev_person_num = 0
    for index, person_num in enumerate(perm):
        # 中の悪いペアの排除
        if (prev_person_num, person_num) in bad_relations or (person_num, prev_person_num) in bad_relations:
            prev_person_num = person_num
            break
        else:
            temp += A[person_num][index]
            prev_person_num = person_num
    else:
        # breakせずに終了できた場合のみmin_timeの更新を行う(for-else構文)
        min_time = min(min_time, temp)


print(-1 if min_time == math.inf else min_time)
