from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    D = int(stdin.readline())
    N = int(stdin.readline())

    diffs = [0]*(D+1)

    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        diffs[L-1] += 1
        diffs[R] -= 1

    temp_height = 0
    for diff in diffs[:-1]:
        temp_height += diff
        print(temp_height)


if __name__ == '__main__':
    main()
