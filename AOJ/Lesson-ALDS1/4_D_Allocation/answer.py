'''
2分探索を用いてO(NlogP)で計算を行う
●方針
最大積載量をPとした時、荷物をk台のトラックに詰め込めるかどうかを検査する関数を実装する(この判定はO(N)で行える)
ニ分探索でその関数を用いてPが可能かどうかをチェックする
'''

from sys import stdin
import math

N, track_num = map(int, stdin.readline().split())

weights = [int(stdin.readline()) for _ in range(N)]


'''
指定の最大積載量Pでk台のトラックに荷物を積み込めるかどうかを判定する関数
※この時、荷物が流れてくる順番は固定されており、制御できない。
 例えば、weights = [8, 1, 7, 3, 9] と weights = [8, 9, 7, 3, 1] では、流れてくる荷物の順番が違うことによって、
 最大積載量が変わるが、順番は考慮しないので、これらの場合は別々の答えを出しても良い。
'''


def can_be_loaded_with_specified_load_capacity(load_capacity):
    track_index = 0
    w_index = 0
    while w_index < N and track_index < track_num:
        tmp_sum = 0
        while w_index < N and tmp_sum + weights[w_index] <= load_capacity:
            tmp_sum += weights[w_index]
            w_index += 1
        track_index += 1
    # w_indexの方が先にNまでインクリメントされた場合、指定のload_capacityで荷物を積むことが可能ということ
    return w_index == N


left = max(weights)-1
right = sum(weights)+1
mid = (left + right) // 2
ans = math.inf

while left <= right:
    if can_be_loaded_with_specified_load_capacity(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
    mid = (left + right) // 2

print(ans)
