from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    A, B = map(int, stdin.readline().split())

    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
    if A < B:
        A, B = B, A

    print(gcd(A, B))


if __name__ == '__main__':
    main()
