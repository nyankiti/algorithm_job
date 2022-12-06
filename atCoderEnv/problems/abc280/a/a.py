from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    ans = 0
    for _ in range(H):
        S = input()
        ans += S.count("#")
    print(ans)


if __name__ == '__main__':
    main()
