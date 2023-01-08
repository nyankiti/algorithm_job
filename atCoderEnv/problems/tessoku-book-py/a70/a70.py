from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    graph = [[] for _ in range(2**N)]
    for _ in range(M):
        X, Y, Z = map(lambda x: int(x)-1, stdin.readline().split())
        for d in range(2**N):
            # d_li = list(map(int, list(format(d, "0"+str(N)+"b"))))
            # # 0, 1 の反転は以下のようにできる
            # d_li[X] = 1 - d_li[X]
            # d_li[Y] = 1 - d_li[Y]
            # d_li[Z] = 1 - d_li[Z]
            # target = 0
            # for i, val in enumerate(d_li):
            #     if val == 1:
            #         target += 2**i
            # 上の方法では3つWAしたが、以下のようにするとACした
            flip = 0
            for j in range(10):
                if j in [X, Y, Z]:
                    flip += 2**j
            target = d ^ flip
            graph[d].append(target)
            graph[target].append(d)

    start = 0
    for i, a in enumerate(A):
        if a == 1:
            start += 2**i

    # bfsする
    dq = deque()
    dist = [-1]*(2**N)
    dq.append(start)
    dist[start] = 0

    while dq:
        popped = dq.popleft()
        for adj in graph[popped]:
            if dist[adj] == -1:
                dist[adj] = dist[popped] + 1
                dq.append(adj)
    print(dist[2**N-1])


if __name__ == '__main__':
    main()
