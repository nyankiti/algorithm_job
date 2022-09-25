import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # 山にある残りの石の個数と高橋くんの点数を保持しながらゲームをメモしながら全探索する
    lookpu = {}

    def rec(rest, is_takahashi_turn):
        if (rest, is_takahashi_turn) in lookpu:
            return lookpu[(rest, is_takahashi_turn)]
        # A[0] == 1 であるので、rest == 0 となる瞬間は必ず訪れる
        if rest == 0:
            return 0
        else:
            if is_takahashi_turn:
                ans = 0
            else:
                ans = math.inf

            # A[0] == 1 であるので 必ず 一つは rest - a >= 0 に引っかかり、ansを更新する
            for a in A:
                if rest - a >= 0:
                    # 高橋くんのターンの時のみpointを更新する
                    if is_takahashi_turn:
                        ans = max(ans, a + rec(rest-a, not is_takahashi_turn))
                    # 青木くんのターンではpointを最小になるように返す
                    else:
                        ans = min(ans, rec(rest-a, not is_takahashi_turn))

            lookpu[(rest, is_takahashi_turn)] = ans
            return lookpu[(rest, is_takahashi_turn)]
    print(rec(N, True))


if __name__ == '__main__':
    main()
