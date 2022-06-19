from sys import stdin


def main():
    N = int(stdin.readline())
    kukan = []
    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        kukan.append([L, R])

    kukan.sort(key=lambda x: x[1])
    ans_li = []

    prev_R = kukan[0][1]
    memo_L = kukan[0][0]

    is_continuous = True
    for L, R in kukan[1:]:
        if is_continuous == False:
            memo_L = L

        # 同じ場合は連続にはならない
        if L < prev_R:
            is_continuous = True
            memo_L = min(memo_L, L)
        else:
            memo_i = -1
            for i, val in enumerate(ans_li):
                if L < val[0]:
                    memo_i = i
                    break
            if memo_i != -1:
                ans_li = ans_li[memo_i:]
                ans_li.append([L, R])
            else:
                ans_li.append([memo_L, R])
                is_continuous = False

        prev_R = R

    else:
        if len(ans_li) == 0:
            ans_li.append([memo_L, R])
        else:
            if ans_li[-1] == [memo_L, R]:
                pass
            else:
                ans_li.append([memo_L, R])

    for ans in ans_li:
        print(*ans)


if __name__ == '__main__':
    main()
