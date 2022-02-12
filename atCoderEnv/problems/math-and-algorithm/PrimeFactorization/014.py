N = int(input())

# 素因数分解
Answer = []
LIMIT = int(N ** 0.5)
for i in range(2, LIMIT + 1):
	while N % i == 0:
		N = N // i
		Answer.append(i)

# 素因数に√N以上の数は二つ以上含まれないので、残った数が最後の素数となる
if N >= 2:
	Answer.append(N)

# 出力
print(*Answer)