import math

N = int(input())
R = [int(input()) for _ in range(N)]

result = -math.inf
for i in range(N):
    temp_max_profit = -math.inf
    for j in range(i+1, N):
        temp_max_profit = max(R[j] - R[i], temp_max_profit)

    result = max(result, temp_max_profit)

print(result)
