'''
model answer より自分の解答(016.py)の方が探索回数が少なく、早く動くが、
model answerの方が簡単に実装でき、問題なくACできる。

硬貨の枚数が9999枚に限定されていることを意識して、さっと以下のように実装できた方が、実装時間を短くできると感じた。
'''

import math
from sys import stdin

N = int(stdin.readline())
*coins, = map(int, stdin.readline().split())

x_coin = coins[0]
y_coin = coins[1]
z_coin = coins[2]

result = math.inf

for x in range(9999):
    for y in range(9999):
        if (N - (x_coin*x + y_coin*y)) % z_coin == 0:
            z = (N - (x_coin*x + y_coin*y)) // z_coin
            if x_coin*x + y_coin*y + z_coin*z == N and z >= 0:
                result = min(x + y + z, result)


print(result)
