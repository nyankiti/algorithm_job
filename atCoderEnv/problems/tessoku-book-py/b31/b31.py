from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    print(N//3 + N//5 + N//7 + N//(3*5*7) - N//(3*5) - N//(5*7) - N//(7*3))


if __name__ == '__main__':
    main()
