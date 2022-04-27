from sys import stdin


def main():
    A, B, K = map(int, stdin.readline().split())
    count = 0
    while B > A:
        A *= K
        count += 1

    print(count)


if __name__ == '__main__':
    main()
