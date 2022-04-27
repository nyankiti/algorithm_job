from sys import stdin


def main():
    S = input()
    numbers = "0123456789"
    for num in numbers:
        if num not in S:
            print(num)


if __name__ == '__main__':
    main()
