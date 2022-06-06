from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    *a, = map(int, stdin.readline().split())

    for _ in range(N // K):
        for i in range(N):
            if i + K < N:
                if a[i] >= a[i+K]:
                    a[i], a[i+K] = a[i+K], a[i]

    for i in range(N-1):
        if a[i] > a[i+1]:
            print("No")
            break
    else:
        print("Yes")


if __name__ == '__main__':
    main()
