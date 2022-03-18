"""
参考：https://twitter.com/e869120/status/1396960059796582400/photo/1

1分使うごとに取れる点数に分けてしまうのがポイント。
1分でとることができる点数は、B点 と B-A点(部分点を最初の1分でとった後、さらに1分使うことで得られる点数)

1分ごとに取れる値を降順に並べ、index = K までの和が最高得点となる

ここで、B > A-B が確定していることが重要
B > A-B が確定しているので、B の先に A-B が選ばれることはなく、部分点をとっていないのに、満点を取るというおかしな事態が発生しない。
"""

from sys import stdin

N, K = map(int, stdin.readline().split())

scores = []
for _ in range(N):
    A, B, = map(int, stdin.readline().split())
    scores.append(B)
    scores.append(A-B)

# スコアが高い順に降順に並べる
scores.sort(reverse=True)

ans = sum(scores[:K])
print(ans)
