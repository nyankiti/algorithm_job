from sys import stdin


def main():
    N = int(stdin.readline())
    S = input()
    count = 0

    for chr in S:
        if chr == "(":
            count += 1
        elif chr == ")":
            count -= 1
        if count < 0:
            print("No")
            return

    print("Yes" if count == 0 else "No")


if __name__ == '__main__':
    main()
