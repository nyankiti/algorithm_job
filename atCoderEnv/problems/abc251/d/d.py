from sys import stdin


def main():
    W = int(stdin.readline())
    ans = []
    # 100進数を使えば、a*100^2 + b * 100^1 + c で全ての数字を表現できる
    for i in range(1, 100):
        for j in range(0, 3):
            w = i * 100 ** j
            ans.append(w)

    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
