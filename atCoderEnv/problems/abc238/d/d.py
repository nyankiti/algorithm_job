from sys import stdin


def main():
    N = int(stdin.readline())
    for _ in range(N):
        a, s = map(int, stdin.readline().split())

        a_bin = bin(a)[2:]
        s_bin = bin(s)[2:]

        # 頭の0の数の調整
        if len(a_bin) > len(s_bin):
            s_bin = "0"*(len(a_bin) - len(s_bin)) + s_bin
        elif len(a_bin) < len(s_bin):
            a_bin = "0"*(len(s_bin)-len(a_bin)) + a_bin

        print("sum", s, s_bin)
        print("and", a, a_bin)

        room = 0
        for i in range(len(a_bin)):
            if a_bin[i] == "0":
                room += pow(2, i)

        if a*2 <= s and s <= a*2 + room:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
