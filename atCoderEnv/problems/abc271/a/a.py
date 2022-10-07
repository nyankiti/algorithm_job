from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    hex_str = str(hex(N))[2:]
    if len(hex_str) == 1:
        hex_str = "0" + hex_str
    print(hex_str.upper())


if __name__ == '__main__':
    main()
