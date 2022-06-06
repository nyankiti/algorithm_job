from sys import stdin


def main():
    N = int(stdin.readline())

    num = 1
    for _ in range(1, 61):
        if N == num-1:
            print("Second")
            break
        num *= 2
    else:
        print("First")


if __name__ == '__main__':
    main()
