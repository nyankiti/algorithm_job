import math


# 逆転の発想を使う。
# ある時間tに買った時、それ以降で最も価値が上がる時間を探したので、毎度探索をする必要があり、計算量がO(n^2)になった。
# 逆転の発想として、
# ある時間tに買った時、それ以前で最も価値が下がる時間を探しても、結果的に最大利益を求められる。
# この方法で探索すると、それ以前で最も価値が下がる時間を記憶しておけるので、計算量がO(n)に抑えられる！！
# この方法を使うと、配列を定義する必要もないので、メモリ使用量も抑えられる。
N = int(input())
prev_min = math.inf
ans = -math.inf
for i in range(N):
    r = int(input())
    # ansを計算するのは、1回目のループ以降(ループの初回はansの計算をしない)

    ans = max(ans, r - prev_min)
    # 最小値の更新
    prev_min = min(prev_min, r)
print(ans)