from sys import stdin
import heapq


def main():
    N, K = map(int, stdin.readline().split())
    *P, = map(int, stdin.readline().split())

    que = P[:K]
    print(min(que))

    # heapの作成
    heapq.heapify(que)
    for i in range(K, N):
        minimum = max(heapq.heappop(que), P[i])
        heapq.heappush(que, minimum)
        ans = heapq.heappop(que)
        print(ans)
        heapq.heappush(que, ans)


if __name__ == '__main__':
    main()
