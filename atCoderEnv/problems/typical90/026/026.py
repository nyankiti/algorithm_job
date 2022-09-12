from sys import stdin, setrecursionlimit
from typing import Counter

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        A, B = map(int, stdin.readline().split())
        tree[A-1].append(B-1)
        tree[B-1].append(A-1)

    # それぞれの頂点の色を判別するための配列。
    # 1: 黒、0: 白、-1: 未訪問
    colors = [-1]*N

    # グラフが二部グラフかどうかのフラグ(この問題では木が与えられているので、グラフが二部グラフであることは確定している)
    is_bipartite = True

    def dfs(v, current_color=0):
        colors[v] = current_color
        for adjacent in tree[v]:
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

    # print("Yes" if is_bipartite else "No")
    # print(colors)

    counter = Counter(colors)
    greater_color = 0
    if counter[0] < counter[1]:
        greater_color = 1

    output_count = 0
    ans = []
    for v, color in enumerate(colors):
        if color == greater_color:
            ans.append(v+1)
            output_count += 1

        if output_count == N//2:
            break

    print(*ans)


if __name__ == '__main__':
    main()
