from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *P, = map(int, stdin.readline().split())

    # 与えられた配置で喜ぶ人の人数を算出するメソッド
    def check(li):
        res = 0
        for i, p in enumerate(li):
            if i == p or i == li[(i-1) % N] or i == li[(i+1) % N]:
                res += 1
        return res

    # とりあえず全探索を実装してみる
    ans = 0
    for i in range(N):
        ans = max(ans, check(P[i:]+P[:i]))
    print(ans)


if __name__ == '__main__':
    main()
