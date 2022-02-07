N = int(input())
li = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(0, N-i-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
            count += 1

print(*li)
print(count)
