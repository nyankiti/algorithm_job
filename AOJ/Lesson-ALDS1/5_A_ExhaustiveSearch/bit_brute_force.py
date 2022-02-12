# Exhausitive searchとはしらみつぶし探索のことで、別名 "Brute-force search"
from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
*table, = map(int, stdin.readline().split())
q = int(stdin.readline())
*M, = map(int, stdin.readline().split())

'''
all_combinations = []
for i in range(2**n):
    tmp_sum = 0
    for j in range(n):
        if ((i >> j) & 1):
            tmp_sum += table[j]
    all_combinations.append(tmp_sum)

for m in M:
    if m in all_combinations:
        print("yes")
    else:
        print("no")

# 約7.1sかかったが、ぎりぎりACされた
'''


# 配列からinを用いて存在チェックするには計算量が嵩張ってしまうので、以下のようハッシュマップを使うと少し早くなる
flags = defaultdict(lambda: False)

for i in range(2**n):
    tmp_sum = 0
    for j in range(n):
        if ((i >> j) & 1):
            tmp_sum += table[j]
    flags[tmp_sum] = True

for m in M:
    if flags[m]:
        print("yes")
    else:
        print("no")

# 約5.2sかかってACされた
