from sys import stdin


def main():
    N, K, A = map(int, stdin.readline().split())
    for _ in range(K-1):
        A += 1
        if A == N+1:
            A = 1
    print(A)


if __name__ == '__main__':
    main()
