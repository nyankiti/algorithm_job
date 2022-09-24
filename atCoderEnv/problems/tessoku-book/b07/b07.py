from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    T = int(stdin.readline())
    N = int(stdin.readline())

    shift = [0]*(T+1)

    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        shift[L] += 1
        shift[R] -= 1

    shift_num = 0
    for diff in shift[:-1]:
        shift_num += diff
        print(shift_num)


if __name__ == '__main__':
    main()
