from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, S = map(int, stdin.readline().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, stdin.readline().split())
        A.append(a)
        B.append(b)

    first_A = A[:N//4]
    second_A = A[N//4:N//2]
    third_A = A[N//2:3*N//4]
    fourth_A = A[3*N//4:]
    print(A)
    print(first_A)
    print(second_A)
    print(third_A)
    print(fourth_A)

    first_B = A[:N//4]
    second_B = A[N//4:N//2]
    third_B = A[N//2:3*N//4]
    fourth_B = B[3*N//4:]


if __name__ == '__main__':
    main()
