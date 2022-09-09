from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    # 雪が積もる問題と同じ。高さの変化を配列に記録する
    sabun = [0]*10**9+1
    for _ in range(N):
        A, B = map(int, stdin.readline().split())
        sabun[A] += 1
        sabun[A+B] -= 1

    height = 0
    ans = {}
    for i in range(N):
        ans[i+1] = 0

    for diff in sabun:
        height += diff
        if height > 0:
            ans[height] += 1

    # print(sabun)
    # print(ans)
    for i in range(N):
        print(ans[i+1], end=" ")
    print()


if __name__ == '__main__':
    main()
