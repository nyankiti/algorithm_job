from collections import Counter, defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A_counter = Counter(A)

    A_li_uni = list(set(A))
    A_li_uni.sort()
    # print(A_li_uni)
    len_A_uni = len(A_li_uni)

    # あるkey aより大きい数字の種類を記録
    shurui_count = {}
    for i, a in enumerate(A_li_uni):
        shurui_count[a] = len_A_uni-i-1
    # print(shurui_count)

    # keyが種類の数、valがその数のaの配列
    shurui_li = defaultdict(list)
    for key, value in shurui_count.items():
        shurui_li[value].append(key)

    # print(shurui_li)

    for k in range(N):
        ans = 0
        for val in shurui_li[k]:
            ans += A_counter[val]
        print(ans)


if __name__ == '__main__':
    main()
