N = int(input())
numbers = list(map(int, input().split()))


def get_GCD(A, B):
	while A >= 1 and B >= 1:
		if A < B:
			B = B % A  # A < B の場合、大きい方 B を書き換える
		else:
			A = A % B  # A >= B の場合、大きい方 A を書き換える
    # 0じゃない方を返す
	return max(A,B)

# 答えを求める
ans = get_GCD(numbers[0], numbers[1])
for i in range(2, N):
	ans = get_GCD(ans, numbers[i])

# 出力
print(ans)