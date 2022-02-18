a, b, c = map(int, input().split())

count = 0
for i in range(a, b+1):
    print(i)
    if c % i == 0:
        count += 1
print(count)
