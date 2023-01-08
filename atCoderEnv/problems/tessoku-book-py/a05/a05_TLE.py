from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())

    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i + j > K:
                break
            for k in range(1, N+1):
                if i + j + k == K:
                    ans += 1
                elif i + j + k > K:
                    break
    print(ans)


if __name__ == '__main__':
    main()
