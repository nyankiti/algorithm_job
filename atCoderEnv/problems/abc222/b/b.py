from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, P = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    count = 0
    for a in A:
        if a < P:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
