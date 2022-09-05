from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        U, V = map(int, stdin.readline().split())
        graph[U].append(V)
        graph[V].append(U)

    ans = 0
    for a in range(1, N+1):
        for b in graph[a]:
            if a < b:
                for c in graph[b]:
                    if b < c and a in graph[c]:
                        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
