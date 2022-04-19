from sys import stdin
from collections import deque

def main():
    dq = deque()
    N = int(stdin.readline())
    for _ in range(N):
        *query, = map(int, stdin.readline().split())
        if query[0] == 0:
            if query[1] == 0:
                dq.appendleft(query[2])
            elif query[1] == 1:
                dq.append(query[2])
        elif query[0] == 1:
            print(dq[query[1]])
        else:
            if query[1] == 0:
                dq.popleft()
            elif query[1] == 1:
                dq.pop()




if __name__ == '__main__':
    main()