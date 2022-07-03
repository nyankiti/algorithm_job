from sys import stdin


def main():
    N = int(stdin.readline())
    for _ in range(N):
        a, s = map(int, stdin.readline().split())

        if a*2 <= s and (s-2*a) & a == 0:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
