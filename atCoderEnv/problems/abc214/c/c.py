from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *S, = map(int, stdin.readline().split())
    *T, = map(int, stdin.readline().split())
    # それぞれが時刻 T_i にもらう宝石を一周させる
    for i in range(N):
        T[i] = min(T[i], T[i-1]+S[i-1])
    # N番目の人の宝石を一周することを考えると、少なくとも 2 周探索する必要があるのがこの問題のミソ！
    for i in range(N):
        T[i] = min(T[i], T[i-1]+S[i-1])
    for val in T:
        print(val)


if __name__ == '__main__':
    main()
