from sys import stdin, setrecursionlimit
from collections import defaultdict
from itertools import combinations
setrecursionlimit(10**6)


def main():
    N, M, K = map(int, stdin.readline().split())
    connections = defaultdict(list)
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        connections[A].append(B)
        connections[B].append(A)
    ans = 0
    for pattern in combinations(range(1, N), K-1):
        target_bars = [0] + list(pattern) + [N]
        j = 0
        temp = 0
        visited = defaultdict(bool)
        for i in range(1, N+1):
            for adj in connections[i]:
                if j+1 < len(target_bars) and target_bars[j] < adj and adj <= target_bars[j+1] and visited[(min(i, adj), max(i, adj))] == False:
                    temp += 1
                    visited[(min(i, adj), max(i, adj))] = True
            if j+1 < len(target_bars) and i == target_bars[j+1]:
                j += 1
                visited = defaultdict(bool)
        # print(pattern, temp)
        ans = max(ans, temp)

    print(ans)


if __name__ == '__main__':
    main()
