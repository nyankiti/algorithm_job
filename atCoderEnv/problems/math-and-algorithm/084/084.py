from sys import stdin


def main():
    a, b, c = map(int, stdin.readline().split())
    if c-a-b > 0:
        if 4*a*b < (c-a-b)*(c-a-b):
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == '__main__':
    main()
