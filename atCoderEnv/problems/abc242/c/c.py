from sys import stdin

N = int(stdin.readline())
MOD = 998244353


# N=1の時
memo = [1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(N-1):
    temp_memo = memo[:]
    for j in range(1, 10):
        if j == 1:
            memo[0] = (temp_memo[0] + temp_memo[1]) % MOD
        elif j == 9:
            memo[8] = (temp_memo[7] + temp_memo[8]) % MOD
        else:
            memo[j-1] = (temp_memo[j-2] + temp_memo[j-1] + temp_memo[j]) % MOD


ans = sum(memo) % MOD
print(ans)
