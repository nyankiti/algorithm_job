from sys import stdin
import heapq


heap_data = []

Q = int(stdin.readline())

for i in range(Q):
    *query, = map(int, stdin.readline().split())
    if query[0] == 1:
        # heapq.heappush(heap_data, query[1])
        heap_data.append(query[1])
    elif query[0] == 2:
        temp_heap = [x for x in heap_data if x <= query[1]]

        heapq.heapify(temp_heap)

        if len(temp_heap) < query[2]:
            print(-1)
            continue
        # print("大きい方から{}番目".format(query[2]))
        res = heapq.nlargest(query[2], temp_heap)
        # print(res)
        print(res[-1])

    elif query[0] == 3:
        temp_heap = [x for x in heap_data if x >= query[1]]

        heapq.heapify(temp_heap)

        if len(temp_heap) < query[2]:
            print(-1)
            continue

        # print("小さい方から{}番目".format(query[2]))
        res = heapq.nsmallest(query[2], temp_heap)
        # print(res)
        print(res[-1])
