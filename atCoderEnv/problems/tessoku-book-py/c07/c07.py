from sys import stdin, setrecursionlimit
import bisect
setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *C, = map(int, stdin.readline().split())
    C.sort()
    ruiseki = [0]
    for cost in C:
        ruiseki.append(ruiseki[-1]+cost)

    Q = int(stdin.readline())
    for _ in range(Q):
        X = int(stdin.readline())
        idx = bisect.bisect_left(ruiseki, X)
        if idx < len(ruiseki) and ruiseki[idx] == X:
            print(idx)
        else:
            print(idx-1)


if __name__ == '__main__':
    main()
