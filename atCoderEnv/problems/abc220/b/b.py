from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    K = int(stdin.readline())
    A, B = input().split()

    A_de = 0
    B_de = 0

    for i in range(len(A)):
        A_de += (int(A[-(i+1)]))*(K**(i))

    for i in range(len(B)):
        B_de += (int(B[-(i+1)]))*(K**(i))

    print(A_de*B_de)


if __name__ == '__main__':
    main()
