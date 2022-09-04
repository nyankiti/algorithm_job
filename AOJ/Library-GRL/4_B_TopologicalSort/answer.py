from collections import deque
from sys import stdin


def main():
    vertices, edges = map(int, stdin.readline().split())

    graph = [[] for _ in range(vertices)]
    # 各頂点の入り次数を格納する配列
    indegrees = [0] * vertices

    for _ in range(edges):
        # s から t への有向edgeが与えられる
        s, t = map(int, stdin.readline().split())
        graph[s].append(t)
        indegrees[t] += 1
    """
    以下の操作を繰り返し、全ての頂点を取り除いた後に得られる配列がトポロジカルソートされている！
    1. 入次数0の頂点vを発見する。
    2. 頂点vを配列の末尾に追加する。
    3. 有向グラフから頂点vと、その頂点から出ている辺をすべて削除する
    """

    def topological_sort(graph, indegrees):
        result = []

        dq = deque()
        # 入り次数が 0 の頂点を記録する
        for i, val in enumerate(indegrees):
            if val == 0:
                dq.append(i)

        while dq:
            v = dq.pop()

            # その頂点と隣接している頂点の入り次数を減らし、0になればdqに追加する
            for u in graph[v]:
                indegrees[u] -= 1
                if indegrees[u] == 0:
                    dq.append(u)

            # 頂点 v を配列の末尾に追加する
            result.append(v)

        return result

    ans = topological_sort(graph, indegrees)
    for val in ans:
        print(val)


if __name__ == '__main__':
    main()