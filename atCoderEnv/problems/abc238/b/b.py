import sys
n = int(input())
A = list(map(int, input().split()))

if n == 1:
    diff = 360-A[0] 
    print(max(diff, A[0]))
    sys.exit()

# その時点での和が合計回転角度となる　回転角度は360と法の元に合同
S_A = []
temp_sum = 0
for a in A:
    temp_sum += a
    S_A.append(temp_sum % 360)

S_A.sort()
# 最初に切れ込みが入るので、0を追加
S_A.insert(0, 0)
#　差が最も大きものの探索
result = 0
for i in range(0, n-1):
    diff = abs(S_A[i] - S_A[i+1])
    result = max(result, diff)

print(result)
