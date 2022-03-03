from sys import stdin
import heapq


heap_data = []

Q = int(stdin.readline())

for i in range(Q):
    *query, = map(int, stdin.readline().split())
    if query[0] == 1:
        heapq.heappush(heap_data, query[1])
    elif query[0] == 2:
        res = heapq.nlargest(query[2]+10, heap_data)
        tmp = []
        
        count = 0
        index = 0
        while count < query[2] and index < len(res):
            if res[index] <= query[1]:
                tmp.append(res[index])
                if count == query[2]:
                    print(res[index])
                    break
                count += 1
            index += 1
        
        if len(tmp) < query[2]:
            print(-1)
            continue
        print(tmp[-1])

    elif query[0] == 3:
        res = heapq.nsmallest(query[2]+10, heap_data)
        tmp = []
        
        count = 0
        index = 0
        while count < query[2] and index < len(res):
            if res[index] >= query[1]:
                tmp.append(res[index])
                count += 1
            index += 1
        
        if len(tmp) < query[2]:
            print(-1)
            continue
        print(tmp[-1])
        
