from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    # 雪が積もる問題と同じ。高さの変化を配列に記録する
    sabun = {}
    for _ in range(N):
        A, B = map(int, stdin.readline().split())
        sabun[A] = sabun.get(A, 0) + 1
        sabun[A+B] = sabun.get(A+B, 0) - 1

    height = 0
    ans = {}
    for i in range(N):
        ans[i+1] = 0

    keys = sorted(sabun.keys())
    prev = keys[0]
    height = sabun[keys[0]]

    for key in keys[1:]:
        day_count = key - prev
        if height > 0:
            ans[height] += day_count

        height += sabun[key]
        prev = key

    # print(sabun)
    # print(ans)
    for i in range(N):
        print(ans[i+1], end=" ")
    print()


if __name__ == '__main__':
    main()
