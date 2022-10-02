from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, X, Y = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    xor_sum = 0
    for a in A:
        a %= 5
        if a < 2:
            x = 0
        elif a < 4:
            x = 1
        else:
            x = 2
        xor_sum ^= x
    print("First" if xor_sum != 0 else "Second")


if __name__ == '__main__':
    main()
