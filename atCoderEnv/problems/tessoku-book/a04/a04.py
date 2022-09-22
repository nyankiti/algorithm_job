from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    bin_N = str(bin(N))[2:]
    if len(bin_N) < 10:
        pre_zero_num = 10 - len(bin_N)
        bin_N = "0"*pre_zero_num + bin_N
    print(bin_N)


if __name__ == '__main__':
    main()
