import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    X, Y = map(int, stdin.readline().split())
    bentou = [list(map(int, stdin.readline().split())) for _ in range(N)]

    # i番目の弁当について、それまでに手に入れたたこ焼きの数、たい焼きの数、選んだ弁当の数

    def rec(i, tako, tai, count):
        if tako >= X and tai >= Y:
            return count
        elif i >= N:
            return 1000
        else:
            ans = math.inf
            # i番目の弁当を買う場合
            ans = min(
                ans, rec(i+1, tako + bentou[i][0], tai + bentou[i][1], count+1))

            # i番目の弁当を買わない場合
            ans = min(ans, rec(i+1, tako, tai, count))
            return ans
    ans = rec(0, 0, 0, 0)
    print(ans if ans != 1000 else "-1")


if __name__ == '__main__':
    main()
