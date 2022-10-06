from collections import Counter
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, color = stdin.readline().split()
    N = int(N)
    A = input()
    c = Counter(A)

    # R, B, W それぞれの数が変わらないことに注目する
    lookup = {}

    def rec(R_count, B_count, W_count):
        if R_count > c["R"]+1 or B_count > c["B"]+1 or W_count > c["W"]+1:
            lookup[(R_count, B_count, W_count)] = True
            return
        if R_count == c["R"] and B_count == c["B"] and W_count == c["W"]:
            print("Yes")
            exit()
        if (R_count, B_count, W_count) in lookup:
            return lookup[(R_count, B_count, W_count)]
        # Rを一つ変換する
        rec(R_count, B_count, W_count+1)
        rec(R_count-1, B_count+2, W_count)
        # Bを一つ変換する
        # rec(R_count, B_count, W_count+1)
        rec(R_count+2, B_count-1, W_count)
        # Wを一つ変換する
        rec(R_count+1, B_count+1, W_count-1)
        # rec(R_count, B_count, W_count+1)

    if color == "R":
        rec(1, 0, 0)
    elif color == "B":
        rec(0, 1, 0)
    else:
        rec(0, 0, 1)

    print("No")


if __name__ == '__main__':
    main()
