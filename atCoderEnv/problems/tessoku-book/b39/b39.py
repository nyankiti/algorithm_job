from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, D = map(int, stdin.readline().split())
    XY = [list(map(int, stdin.readline().split())) for _ in range(N)]
    # XY.sort(key=lambda x: x[0])
    # print(XY)
    works = {}
    for x, y in XY:
        if works.get(x):
            works[x].append(y)
        else:
            works[x] = [y]

    available_works = []
    ans = 0

    for day in range(1, D+1):
        if works.get(day):
            available_works.extend(works[day])
        if len(available_works) > 0:
            max_val = max(available_works)
            ans += max_val
            max_idx = available_works.index(max_val)
            available_works.pop(max_idx)

    print(ans)


if __name__ == '__main__':
    main()
