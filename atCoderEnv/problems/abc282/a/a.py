from sys import stdin, setrecursionlimit
import string

setrecursionlimit(10**6)


def main():
    K = int(stdin.readline())
    print(string.ascii_uppercase[:K])


if __name__ == '__main__':
    main()
