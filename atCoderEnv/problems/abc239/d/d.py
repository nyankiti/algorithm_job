from sys import stdin, exit


# Fermat's little theorem
def is_prime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        return 2**(x-1) % x == 1



'''
高橋くんがある整数 X を選んだとします。X+Y が素数になる整数 Y が C 以上 D 以下に 1 つでもあれば、それを選べば青木君の勝ちです。1 つもなければ、高橋君の勝ちです。

高橋君が選ぶ A 以上 B 以下 の整数を全探索します。さらに、高橋君が選んだ各整数に対して、青木君が選ぶ C 以上 D 以下の整数も全探索し、高橋君が勝てるかどうかを判定します。

高橋君が勝てるパターンが一つでもあれば高橋君の勝ちで、そうでなければ青木君の勝ちです。
'''

def solve():
    def judge(x):
        for y in range(C, D + 1):
            if is_prime(x + y):
                return False
        return True

    A, B, C, D = map(int, stdin.readline().split())
    for x in range(A, B + 1):
        if judge(x):
            return True
    return False

print("Takahashi" if solve() else "Aoki")