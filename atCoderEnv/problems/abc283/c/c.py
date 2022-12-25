from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    zerozero_count = S.count("00")
    print(len(S)-zerozero_count)


if __name__ == '__main__':
    main()
