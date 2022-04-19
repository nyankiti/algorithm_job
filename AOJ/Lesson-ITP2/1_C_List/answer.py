from sys import stdin
from collections import deque

def main():
    N = int(stdin.readline())
    cursor = 0
    li = []
    for _ in range(N):
        *query, = map(int, stdin.readline().split())
        if query[0] == 0:
            # insert
            li.insert(cursor, query[1])
            cursor += 1
        elif query[0] == 1:
            # move
            cursor -= query[1]
        else:
            del li[cursor-1]
            cursor -= 1

    for val in reversed(li):
        print(val)




if __name__ == '__main__':
    main()
