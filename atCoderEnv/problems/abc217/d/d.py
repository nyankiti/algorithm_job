from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)


def main():
    L, Q = map(int, stdin.readline().split())
    # union findを逆向きに実装する
    split_point = [0, L]
    for _ in range(Q):
        c, x = map(int, stdin.readline().split())
        if c == 1:
            bisect.insort_left(split_point, x)
        elif c == 2:
            r = bisect.bisect_left(split_point, x)
            print(split_point[r]-split_point[r-1])


if __name__ == '__main__':
    main()
