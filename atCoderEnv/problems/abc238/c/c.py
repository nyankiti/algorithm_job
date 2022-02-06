N = int(input())

def get_tousasuuretu_sum(n):
    return (n*(2+n-1))//2

result = 0

# 直前の桁まではまとめて計算する
N_digit = len(str(N))
for i in range(1,N_digit):
    kousuu = int("9".ljust(i, "0"))
    # print(kousuu)
    # 項差1の等差数列の和を計上する
    result += get_tousasuuretu_sum(kousuu)

start = 10**(N_digit-1)
# print(start)
result += get_tousasuuretu_sum(N-start+1)

print(result%998244353)
