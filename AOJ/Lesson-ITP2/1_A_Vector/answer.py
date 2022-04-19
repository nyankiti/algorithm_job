from sys import stdin
from collections import deque

def main():
    dq = deque()
    N = int(stdin.readline())
    for _ in range(N):
        *query, = map(int, stdin.readline().split())
        if query[0] == 0:
            dq.append(query[1])
        elif query[0] == 1:
            print(dq[query[1]])
        else:
            dq.pop()




if __name__ == '__main__':
    main()