from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())

    ans = 0
    for i in range(1, N+1):
        for j in range(max(1, i-K), min(N+1, i+K)):
            for k in range(max(1, j-K), min(N+1, j+K)):
                if abs(j-k) <= K-1 and abs(i-k) <= K-1 and abs(i-j) <= K-1:
                    ans += 1

    print(N*N*N - ans)


if __name__ == '__main__':
    main()
