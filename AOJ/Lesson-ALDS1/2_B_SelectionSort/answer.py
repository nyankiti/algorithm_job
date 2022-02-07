# N = int(input())
# li = list(map(int, input().split()))

# count = 0
# for i in range(N):
#     temp_min_index = i
#     for j in range(i, N):
#         if li[temp_min_index] > li[j]:
#             temp_min_index = j
#     if i != temp_min_index:
#         li[i], li[temp_min_index] = li[temp_min_index], li[i]
#         count += 1

# print(*li)
# print(count)


# コードを短くしたバージョン-------------------------------------------------------
n = int(input())
*A, = map(int, input().split())

count = 0
for i in range(n):
    j = A[i:].index(min(A[i:])) + i
    A[i], A[j] = A[j], A[i]
    if i != j:
        count += 1
print(*A)
print(count)
