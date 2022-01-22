import itertools

K = int(input())

# 桁の決定
digit = 1

while True:
    if 2**digit < K and 2**(digit+1) > K:
        break
    digit += 1

# その桁の前までの数字の数の和
count = (2**(digit)) - 1

# 答えとの差
diff_count = K - count

result = []

for i in range(digit):
    temp = diff_count % 2**(i+1)
    # print(temp)
    if temp == 0:
        result.append("2")
        continue
    if temp > 2**(i):
        result.append("2")
    else:
        result.append("0")

result.append("2")
result.reverse()
print("".join(result))
