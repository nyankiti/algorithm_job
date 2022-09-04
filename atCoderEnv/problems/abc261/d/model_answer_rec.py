from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def main():
    N, M = map(int, stdin.readline().split())
    *X, = map(int, stdin.readline().split())

    bonus = {}
    for i in range(M):
        C, Y = map(int, stdin.readline().split())
        bonus[C] = Y

    lookup = {}

    def rec(n, counter):
        if (n, counter) in lookup:
            return lookup[(n, counter)]

        # base case
        if n == 1 and counter == 0:
            return X[n-1] + bonus.get(counter, 0)

        # もしカウンターが 0 の場合は、前回の値が予想できないので、全て試す必要がある
        if counter == 0:
            candidate = []
            for c in range(0, n):
                candidate.append(rec(n-1, c))

            lookup[(n, counter)] = X[n-1] + max(candidate)
            return lookup[(n, counter)]
        else:
            lookup[(n, counter)] = X[n-1] + \
                bonus.get(counter, 0) + rec(n-1, counter-1)
            return lookup[(n, counter)]

    # 最後のカウンターの数値によって、答えが異なるので、全て試す
    ans_candidate = []
    for i in range(N+1):
        ans_candidate.append(rec(N, i))
    print(ans_candidate)
    print(max(ans_candidate))


if __name__ == '__main__':
    main()
