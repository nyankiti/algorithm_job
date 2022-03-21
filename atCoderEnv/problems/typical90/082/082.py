from sys import stdin

mod = 10 ** 9 + 7
L, R = map(int, stdin.readline().split())


def tousa_sum(N):
    return N*(N+1)//2


# 桁は1 ~ 19までの範囲という制約があるので、それぞれの桁について何回書かれるかを集計する
each_digit_count = [0]*19

L_digit = len(str(L))
R_digit = len(str(R))

if R_digit == L_digit:
    each_digit_count[R_digit-1] = R - L + 1
else:
    for i in range(L_digit, R_digit+1):
        each_digit_count[i-1] = 9 * 10**(i-1)
    # 末端の数字の処理
    each_digit_count[L_digit-1] = 10**L_digit - L
    each_digit_count[R_digit-1] = R - 10**(R_digit-1) + 1


ans = 0
# print(each_digit_count)
first_num = True
for digit, value in enumerate(each_digit_count):

    if value != 0:
        temp_sum = tousa_sum(min(10**(digit+1)-1, R)) - \
            tousa_sum(max(10**digit, L)-1)
        e = (digit+1) * temp_sum
        # print("単純な和", temp_sum)
        # print(e)
        ans = (ans + e) % mod


print(ans)


# つよつよの人の解答
L, R = map(int, input().split())
mod = 10**9+7

first = len(str(L))
last = len(str(R))


def sum_cnt(s, g):
    cnt = (g-s+1)*(s+g)//2
    cnt %= mod
    return len(str(s))*cnt % mod


ans = 0
for i in range(first, last+1):
    start = max(10**(i-1), L)
    goal = min(R, 10**i-1)
    ans += sum_cnt(start, goal)
    ans %= mod

print(ans)
