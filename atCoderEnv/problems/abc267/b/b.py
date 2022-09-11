from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    *S, = map(int, list(input()))

    grid = [[] for _ in range(7)]
    for i in range(len(S)):
        if i+1 == 7:
            grid[0].append(S[i])
        elif i+1 == 4:
            grid[1].append(S[i])
        elif i+1 == 2 or i+1 == 8:
            grid[2].append(S[i])
        elif i+1 == 5 or i+1 == 1:
            grid[3].append(S[i])
        elif i+1 == 9 or i+1 == 3:
            grid[4].append(S[i])
        elif i+1 == 6:
            grid[5].append(S[i])
        elif i+1 == 10:
            grid[6].append(S[i])

    # for row in grid:
    #     print(row)
    # print("-------------")

    if S[0] == 0:
        # ピンが全て倒れている列を探す
        for i in range(1, 6):
            if 1 not in grid[i]:
                # print(str(i)+"は全て倒れているよ")

                # 全て倒れている列より左側に立っているピンが存在するかどうかのチェック
                is_left_ok = False
                for j in range(i):
                    if 1 in grid[j]:
                        is_left_ok = True
                # 全て倒れている列より右側に立っているピンが存在するかどうかのチェック
                is_right_ok = False
                for j in range(i+1, 7):
                    if 1 in grid[j]:
                        is_right_ok = True
                # print(str(i), is_left_ok, is_right_ok)
                if is_left_ok and is_right_ok:
                    print("Yes")
                    return

    print("No")


if __name__ == '__main__':
    main()
