from sys import stdin

coins = [25, 10, 5, 1]
target = int(stdin.readline())
count = 0

for coin in coins:
    quotient = target // coin
    count += quotient
    target = target - (coin * quotient)

print(count)
