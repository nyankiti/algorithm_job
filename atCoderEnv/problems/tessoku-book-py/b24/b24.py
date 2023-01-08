

import bisect
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    boxes = [list(map(int, stdin.readline().split())) for _ in range(N)]

    # Xの昇順でソートし、Xが一致した場合はYの降順でソートする
    boxes.sort(key=lambda x: (x[0], -x[1]))

    # 以下のようにソートすると、Yの値が最適な状態でない場合が生じて、WAしてしまう
    # boxes.sort(key=lambda x: (x[0], x[1]))

    # Yについて 最長増加部分列を求める
    height = [boxes[0][1]]
    for i in range(1, N):
        idx = bisect.bisect_left(height, boxes[i][1])
        if idx >= len(height):
            height.append(boxes[i][1])
        else:
            height[idx] = boxes[i][1]
    print(len(height))


if __name__ == '__main__':
    main()
