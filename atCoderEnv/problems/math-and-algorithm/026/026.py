from sys import stdin

N = int(stdin.readline())


r = 0
for i in range(1, N+1):
    r += 1.0*N / i

print("%.12f" % r)

# 答えの計算
# Answer = 0.0
# for i in range(1, N+1):
#     Answer += 1.0 * N / i

# # 出力
# print("%.12f" % Answer)
