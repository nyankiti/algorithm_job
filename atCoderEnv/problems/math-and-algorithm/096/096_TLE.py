import math
from sys import stdin


def main():
    N = int(stdin.readline())
    *T, = map(int, stdin.readline().split())

    # 和が均等になるように二つのグループに分割できレバ良い => bit全探索？
    ans = math.inf
    for i in range(2**N):
        first_group = 0
        second_group = 0
        for j in range(N):
            if ((i >> j) & 1):
                first_group += T[j]
            else:
                second_group += T[j]

        ans = min(ans, max(first_group, second_group))

    print(ans)


if __name__ == '__main__':
    main()
