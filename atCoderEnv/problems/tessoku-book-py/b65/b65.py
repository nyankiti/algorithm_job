from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, T = map(int, stdin.readline().split())
    # それぞれのnodeのTからの距離を求めれば良い
    tree = [[] for _ in range(N)]

    for _ in range(N-1):
        A, B = map(lambda x: int(x)-1, stdin.readline().split())
        tree[A].append(B)
        tree[B].append(A)

    lookup = {}
    level = [0]*N
    visited = [False]*N

    def rec(v):
        visited[v] = True

        if v in lookup:
            return lookup[v]
        if len(tree[v]) == 1 and visited[tree[v][0]]:
            level[v] = 0
            return 0

        temp_level = 0
        for adj in tree[v]:
            if visited[adj] == False:
                temp_level = max(temp_level, rec(adj))
            else:
                temp_level = max(temp_level, level[adj])

        level[v] = temp_level+1
        lookup[v] = temp_level+1
        return lookup[v]

    rec(T-1)
    print(*level)


if __name__ == '__main__':
    main()
