N = int(input())
A = list(map(int, input().split()))

# 以下に間違ってselection sortを実装してしまった
# for i in range(N):
#     temp_min = math.inf
#     min_index = i
#     for j in range(i, N):
#         if temp_min > A[j]:
#             temp_min = A[j]
#             min_index = j

#     A[i], A[min_index] = A[min_index], A[i]
#     print(*A)


# insertion sort
for i in range(N):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
        # 既にsort済みの部分から、次の対象(v)が入る場所を探す。入る場所が見つかるまで、A[j+1] = A[j] とすることでずらしていく
        A[j+1] = A[j]
        j -= 1
    A[j+1] = v
    print(*A)
