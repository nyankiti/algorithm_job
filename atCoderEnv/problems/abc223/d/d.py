from sys import stdin, exit
import heapq


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    indegrees = [0]*N

    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        A, B = A-1, B-1
        graph[A].append(B)
        indegrees[B] += 1

    # for row in graph:
    #     print(row)
    # print(indegrees)

    def topological_sort(graph, indegrees):
        result = []

        hp = []
        # 入り次数が 0 の頂点を記録する
        for i, val in enumerate(indegrees):
            if val == 0:
                heapq.heappush(hp, i)

        while len(hp) > 0:
            v = heapq.heappop(hp)

            # その頂点と隣接している頂点の入り次数を減らし、0になればdqに追加する
            for i in range(len(graph[v])):
                u = graph[v][i]
                indegrees[u] -= 1
                if indegrees[u] == 0:
                    heapq.heappush(hp, u)
                    # dq.append(u)

            # 頂点 v を配列の末尾に追加する
            result.append(v)

        for val in indegrees:
            if val != 0:
                print(-1)
                exit()
        else:
            return result

    ans = topological_sort(graph, indegrees)
    print(*map(lambda x: x+1, ans))


if __name__ == '__main__':
    main()
