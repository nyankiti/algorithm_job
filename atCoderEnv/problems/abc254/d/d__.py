import math
from sys import stdin


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    N = int(stdin.readline())
    # N = 5

    # 最初に1の分を追加しておく
    ans = 1
    for i in range(2, math.floor(math.sqrt(N))+1):
        fact_ans = factorization(i*i)
        print(i, i*i, fact_ans)
        sub_ans = 1
        for el in fact_ans:
            sub_ans = sub_ans * (el[1]+1)

        ans += sub_ans
        print(sub_ans)
        print("ans", ans)

    ans = ans + (N - math.floor(math.sqrt(N)))
    print(ans)


if __name__ == '__main__':
    main()
