import math
from sys import stdin, exit

N = int(stdin.readline())
*coins, = map(int, stdin.readline().split())

# coinを大きい順に並び替える
coins.sort(key=lambda x: -x)

x_coin = coins[0]
y_coin = coins[1]
z_coin = coins[2]


result = math.inf

for x in range(N//x_coin, -1, -1):
    for y in range(N//y_coin, -1, -1):
        if (N - (x_coin*x + y_coin*y)) % z_coin == 0:
            z = (N - (x_coin*x + y_coin*y)) // z_coin
            if x_coin*x + y_coin*y + z_coin*z == N and z >= 0:
                result = min(x + y + z, result)
                break

    for z in range(N//z_coin, -1, -1):
        if (N - (x_coin*x + z_coin*z)) % y_coin == 0:
            y = (N - (x_coin*x + z_coin*z)) // y_coin
            if x_coin*x + y_coin*y + z_coin*z == N and y >= 0:
                result = min(x + y + z, result)
                break

print(result)
