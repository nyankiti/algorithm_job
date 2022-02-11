# bit全探索による全探索 => TLE  計算量O(N^K)

from sys import stdin
import math

n, track_num = map(int, stdin.readline().split())

weights = [int(stdin.readline()) for _ in range(n)]


def base10int(value, base):
    if (value // base):
        return base10int((value // base), base) + str(value % base)
    return str(value % base)


each_track_weight = [0]*track_num
result = math.inf

# n個の荷物がtrack_num個のトラックに振り分けられるので、その振り分け方は全部で track_num^n パターンある。
# これを、track_num進数に直すと、それぞれの桁の数が、割り当てられるtrackの番号と一致することを利用した全探索。
for i in range(track_num ** n):
    each_track_weight = [0]*track_num
    pattern = str(base10int(i, track_num))
    pattern = pattern.ljust(n, '0')
    for i, track_index in enumerate(pattern):
        each_track_weight[int(track_index)] += weights[i]
    result = min(result, max(each_track_weight))

    print("pattern {}: ".format(pattern))

print(result)
