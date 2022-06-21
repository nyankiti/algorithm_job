from sys import stdin


def main():
    N, X = map(int, stdin.readline().split())

    count = 0
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            for c in range(b+1, N+1):
                if a+b+c == X:
                    count += 1
    print(count)


if __name__ == '__main__':
    main()
