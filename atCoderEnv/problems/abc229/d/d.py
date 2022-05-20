from sys import stdin
from collections import deque


def main():
    S = input()
    K = int(stdin.readline())
    dq = deque()
    remaining_count = K
    ans, score = 0, 0

    for char in S:
        score += 1
        if char == ".":
            dq.append(1)
            remaining_count -= 1
        else:
            dq.append(0)

        while remaining_count < 0:
            remaining_count += dq.popleft()
            score -= 1

        ans = max(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
