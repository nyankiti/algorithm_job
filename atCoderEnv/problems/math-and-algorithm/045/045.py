from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)

    ans = 0
    for i, adjacency_list in enumerate(G):
        count = 0
        for j in adjacency_list:
            if j < i:
                count += 1
        if count == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
