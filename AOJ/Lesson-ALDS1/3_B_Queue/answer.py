# import queue

# n, quants = map(int, input().split())

# q = queue.Queue()
# time = 0

# for i in range(n):
#     line = input().split()
#     q.put((line[0], int(line[1])))

# while not q.empty():
#     process_name, process_time = q.get()
#     diff = process_time - quants
#     if diff > 0:
#         q.put((process_name, diff))
#         time += quants
#     else:
#         time += process_time
#         print(process_name, time)


# queueよりdequeu使った方が圧倒的に早い！！
from collections import deque

n, quants = map(int, input().split())

deq = deque()
time = 0

for i in range(n):
    line = input().split()
    deq.append((line[0], int(line[1])))

while deq:
    process_name, process_time = deq.popleft()
    diff = process_time - quants
    if diff > 0:
        deq.append((process_name, diff))
        time += quants
    else:
        time += process_time
        print(process_name, time)
