from sys import stdin
from collections import deque

from numpy import False_


def main():
    Q = int(stdin.readline())
    dq = deque()
    flg = True
    for _ in range(Q):
        *query, = stdin.readline().split()

        if query[0] == "1":
            dq.extend([int(query[1])]*int(query[2]))
        elif query[0] == "2":
            temp_sum = 0
            for i in range(int(query[1])):
                temp_sum += dq.popleft()
            print(temp_sum)
            flg = False

    if flg:
        print()


if __name__ == '__main__':
    main()
