from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

# メモリエラーっぽい？


def main():
    H, W, r_s, c_s = map(int, stdin.readline().split())
    curr_r = r_s - 1
    curr_c = c_s - 1

    # . がみち、 # が壁
    walls = defaultdict(lambda: ".")
    N = int(stdin.readline())
    for _ in range(N):
        r, c = map(lambda x: int(x)-1, stdin.readline().split())
        walls[(r, c)] = "#"

    Q = int(stdin.readline())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)

        # シミュレーション
        while l > 0:
            if d == "L":
                if curr_c - 1 >= 0 and walls[(curr_r, curr_c-1)] == ".":
                    curr_c -= 1
                    l -= 1
                else:
                    break
            elif d == "R":
                if curr_c + 1 < W and walls[curr_r, curr_c+1] == ".":
                    curr_c += 1
                    l -= 1
                else:
                    break
            elif d == "U":
                if curr_r - 1 >= 0 and walls[curr_r-1, curr_c] == ".":
                    curr_r -= 1
                    l -= 1
                else:
                    break
            elif d == "D":
                if curr_r + 1 < H and walls[curr_r+1, curr_c] == ".":
                    curr_r += 1
                    l -= 1
                else:
                    break

        print(curr_r+1, curr_c+1)


if __name__ == '__main__':
    main()
