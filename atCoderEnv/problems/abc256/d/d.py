from sys import stdin
from collections import deque


def main():
    N = int(stdin.readline())
    number_line = []
    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        number_line.append([R, "R"])
        number_line.append([L, "L"])

    # 同じ値ならば、Lが前に来るように並び替える
    number_line.sort(key=lambda x: x[0])

    prev_val = [-1, "X"]
    for i, val in enumerate(number_line[:]):
        if prev_val[0] == val[0]:
            if prev_val[1] == "R":
                number_line[i-1], number_line[i] = number_line[i], number_line[i-1]
        prev_val = val

    dq = deque()
    ans_li = []
    for val in number_line:
        if val[1] == "L":
            dq.append([val[0], "L"])
        elif val[1] == "R":
            popped = dq.pop()
            if len(dq) == 0:
                ans_li.append([popped[0], val[0]])

    for ans in ans_li:
        print(*ans)


if __name__ == '__main__':
    main()
