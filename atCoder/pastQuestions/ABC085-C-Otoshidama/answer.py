N, Y = map(int, input().split())

count1 = 0
count2 = 0
count3 = 0

while True:
    if N < 10000:
        break
    count1 += 1
    N -= 10000

while True:
    if N < 5000:
        break
    count2 += 1
    N -= 5000

while True:
    if N < 1000:
        break
    count3 += 1
    N -= 1000

if N == 0:
    print(str(count1) + str(count2) + str(count3))
else:
    print("-1 -1 -1")
