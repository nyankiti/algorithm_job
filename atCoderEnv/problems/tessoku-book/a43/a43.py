from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, L = map(int, stdin.readline().split())
    ans = 0
    for _ in range(N):
        A, B = stdin.readline().split()
        if B == "E":
            ans = max(ans, L-int(A))
        elif B == "W":
            ans = max(ans, int(A))
    print(ans)


if __name__ == '__main__':
    main()
