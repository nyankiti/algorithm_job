from sys import stdin


def main():
    N, X = map(int, stdin.readline().split())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    while X > N:
        X -= N
        i += 1
    print(alphabet[i])


if __name__ == '__main__':
    main()
