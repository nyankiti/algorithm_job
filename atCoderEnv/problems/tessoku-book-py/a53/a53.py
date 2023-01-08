from sys import stdin, setrecursionlimit
import heapq


setrecursionlimit(10**6)


def main():
    Q = int(stdin.readline())
    heap_data = []
    for _ in range(Q):
        query = stdin.readline().split()
        if query[0] == "1":
            heapq.heappush(heap_data, int(query[1]))
        elif query[0] == "2":
            print(heapq.nsmallest(1, heap_data)[0])
        else:
            heapq.heappop(heap_data)


if __name__ == '__main__':
    main()
