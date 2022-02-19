from sys import stdin
import heapq

# 標準ライブラリのheapqはmin heapなので、符号を逆にして使う
heap_data = []
while True:
    query = stdin.readline().split()
    if query[0] == "insert":
        heapq.heappush(heap_data, -int(query[1]))
    elif query[0] == "extract":
        print(-heapq.heappop(heap_data))
    else:
        break

'''
03.65 s
45568 KB
21832058 B
2501775 B
5.in
'''
