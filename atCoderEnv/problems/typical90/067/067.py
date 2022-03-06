from sys import stdin

N, K = map(int, stdin.readline().split())

# N進数へ変換するメソッド


# 10進数をn進数へ変換
def base10int(value, base):
    if (value // base):
        return base10int((value // base), base) + str(value % base)
    return str(value % base)


# n進数を10進数に変換
def to10(value, base):
    result = 0
    for index, num in enumerate(str(value)[::-1]):
        result += int(num) * (base ** index)
    return result


for _ in range(K):
    decimal_number = to10(N, 8)
    septic_number = base10int(decimal_number, 9)
    ans = septic_number.replace("8", "5")
    N = ans
print(ans)
