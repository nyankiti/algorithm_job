from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)


def is_bipartite(graph):
    N = len(graph)
    # それぞれの頂点の色を判別するための配列。
    # 1: 黒、0: 白、-1: 未訪問
    colors = [-1]*N

    # グラフが二部グラフかどうかのフラグ(この問題では木が与えられているので、グラフが二部グラフであることは確定している)
    is_bipartite = True

    def dfs(v, current_color=0):
        colors[v] = current_color
        for adjacent in graph[v]:
            # 既に隣接頂点の色が決まっている場合
            if colors[adjacent] != -1:
                if colors[adjacent] == current_color:
                    return False
                continue

            # 1-current_colorとすると、1と
            if dfs(adjacent, 1-current_color) == False:
                return False
        return True

    # 全ての辺を探索する
    for v in range(N):
        if colors[v] != -1:
            continue
        if dfs(v) == False:
            is_bipartite = False

    return is_bipartite


def main():
    # 愚直に全探索
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    existing_pair = defaultdict(bool)
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        # u が小さいようにする
        if u > v:
            u, v = v, u
        existing_pair[(u, v)] = True

    ans = 0

    for i in range(N):
        for j in range(i+1, N):
            if existing_pair[(i, j)] == False:
                graph[i].append(j)
                graph[j].append(i)
                if is_bipartite(graph):
                    ans += 1
                graph[i].pop()
                graph[j].pop()
    print(ans)


if __name__ == '__main__':
    main()
