from sys import stdin


def main():
    a, b, c = map(int, stdin.readline().split())
    if c == 1:
        print('No')
        return

    ans = 1
    for _ in range(b):
        ans *= c
        if ans > a:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
