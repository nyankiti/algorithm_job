import math
from sys import stdin
from typing import List


def check(target_num: str, numbers: List[str]):
    elapsed_time = 0
    visited = [False]*len(numbers)

    while False in visited:
        candidate = 0
        for i in range(10):
            visited_indexes = [False]*10
            for S_index, S in enumerate(numbers):
                if S[i] == target_num:
                    if visited_indexes[S_index] == False and visited[S_index] == False:
                        candidate = max(candidate, i)
                        visited_indexes[S_index] = True
                        visited[S_index] = True

        elapsed_time += candidate

        if False in visited:
            elapsed_time += 10

    print(elapsed_time)

    return elapsed_time


def main():
    N = int(stdin.readline())
    numbers = []
    for _ in range(N):
        S = input()
        numbers.append(S)
    # print(numbers)

    ans = math.inf
    for i in range(10):
        ans = min(ans, check(str(i), numbers))

    print(ans)


if __name__ == '__main__':
    main()
