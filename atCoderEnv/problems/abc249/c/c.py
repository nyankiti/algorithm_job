from sys import stdin
from collections import Counter


def main():
    N, K = map(int, stdin.readline().split())
    S = []
    for _ in range(N):
        S.append(input())

    ans = 0

    for i in range(2**N):
        temp_count = 0
        temp_counter = {}
        for j in range(N):
            if ((i >> j) & 1):
                for char in S[j]:
                    temp_counter[char] = temp_counter.get(char, 0) + 1

        for val in temp_counter.values():
            if val == K:
                temp_count += 1
        ans = max(ans, temp_count)
    print(ans)


if __name__ == '__main__':
    main()
