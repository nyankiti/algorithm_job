from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    bin_N = bin(1024+N-1)[3:]
    # print(bin_N)
    print(bin_N.replace("0", "4").replace("1", "7"))


if __name__ == '__main__':
    main()
