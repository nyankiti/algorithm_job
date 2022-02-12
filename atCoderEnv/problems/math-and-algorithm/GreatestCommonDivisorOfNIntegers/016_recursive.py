#!/usr/bin python
n = int(input())
*numbers, = map(int, input().split())


# a > bとする
def getGCD(a, b):
    # 大きさが逆の場合の対処
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return getGCD(b, c)

ans = numbers[0]
for i in range(1,n):
    ans = getGCD(ans, numbers[i])

print(ans)