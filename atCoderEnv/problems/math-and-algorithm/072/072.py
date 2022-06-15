import math
from sys import stdin


def main():
    A, B = map(int, stdin.readline().split())
    max_ans = B-A
    # prev = -1
    # for i in range(max_ans, 0, -1):
    #     for j in range(A, B+1):
    #         if j % i == 0:
    #             if prev == i:
    #                 print(i)
    #                 return
    #             prev = i
    for i in range(max_ans, 0, -1):
        if math.floor(B/i) - math.ceil(A/i) >= 1:
            print(i)
            return


if __name__ == '__main__':
    main()
