from sys import stdin, setrecursionlimit
import string

setrecursionlimit(10**6)


def main():
    *P, = map(int, stdin.readline().split())
    alphabet = string.ascii_lowercase
    for p in P:
        print(alphabet[p-1], end="")
    print("")


if __name__ == '__main__':
    main()
