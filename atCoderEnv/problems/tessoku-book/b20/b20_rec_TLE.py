from collections import deque
import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

# 「編集距離(レーベンシュタイン距離)」に関する難しい問題!


def main():
    S = input()
    T = input()

    lookup = {}
    # Levenshtein Distance (編集距離)の略

    def get_LD(x, y):
        if (x, y) in lookup:
            return lookup[(x, y)]
        if len(x) == 0:
            return len(y)
        elif len(y) == 0:
            return len(x)
        else:
            # 先頭の文字が同じ時
            if x[0] == y[0]:
                lookup[(x, y)] = get_LD(x[1:], y[1:])
                return lookup[(x, y)]
            else:
                ans = math.inf
                # 消去
                ans = min(ans, get_LD(x[1:], y) + 1)
                ans = min(ans, get_LD(x, y[1:]) + 1)
                # 挿入
                ans = min(ans, get_LD(y[0]+x, y) + 1)
                ans = min(ans, get_LD(x, x[0]+y) + 1)
                # 変換
                ans = min(ans, get_LD(y[0]+x[1:], y) + 1)
                ans = min(ans, get_LD(x, x[0]+y[1:]) + 1)
                lookup[(x, y)] = ans
                return lookup[(x, y)]
    print(get_LD(S, T))


if __name__ == '__main__':
    main()
