from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def check(winning_number, val):
    same_count = 0
    for i in range(4):
        if winning_number[i] == val[i]:
            same_count += 1
    if same_count == 4:
        return 1
    elif same_count == 3:
        return 2
    else:
        return 3


def main():
    N = int(stdin.readline())
    ST = [list(map(int, stdin.readline().split())) for _ in range(N)]
    candidate = []
    for val in range(10000):
        win_num = str(val).zfill(4)
        # 全てがあたりの場合を試す
        for S, T in ST:
            if check(win_num, str(S).zfill(4)) != T:
                break
        else:
            candidate.append(win_num)

    if len(candidate) == 1:
        print(candidate[0])
    elif len(candidate) > 1:
        print("Can't Solve")


if __name__ == '__main__':
    main()
