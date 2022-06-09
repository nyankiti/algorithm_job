from sys import stdin


"""
N個の都市に対して、道路はN-1個で、かつ全ての都市で移動可能 => 閉路はできない(グラフは木構造でしかない)。
さらに言えば、全域木という種類の木を形成している。

全域木では、ある頂点 u から v へ行くパスはただ一つしか存在しない。
=> この問題では、この単純パスが最も長い頂点二つを結べば答えとなる！

一度、木の末端を調べ、その末端から、末端までのパスが答えとなる！！
"""


def main():
    N = int(stdin.readline())
    graph = [[] for _ in range(N)]

    for _ in range(N-1):
        A, B = map(lambda x: int(x)-1, stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    def DFS(start):
        # startからの距離
        distance = [-1]*N
        distance[start] = 0
        next = [start]
        mx, u = -1, -1

        while next:
            v = next.pop()  # 深さ優先で次のnodeを探索する

            # 最大値チェック
            if distance[v] > mx:
                mx = distance[v]
                u = v
            # 次の候補の探索
            for i in graph[v]:
                if distance[i] == -1:
                    distance[i] = distance[v] + 1
                    next.append(i)
        # print(distance, mx, u)

        return mx, u

    zero_to_end, zero_to_end_idx = DFS(0)
    end_to_end, _ = DFS(zero_to_end_idx)
    print(end_to_end+1)

    # for row in graph:
    #     print(row)


if __name__ == '__main__':
    main()
