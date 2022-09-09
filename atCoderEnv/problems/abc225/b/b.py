from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    tree = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, stdin.readline().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)

    for v in tree:
        if len(v) == N-1:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
