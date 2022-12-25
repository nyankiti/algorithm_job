from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    A = [list(map(int, stdin.readline().split())) for _ in range(H)]

    for row in A:
        print(row)


if __name__ == '__main__':
    main()
