from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    a_sum = sum(A)
    if a_sum <= K:
        if (K-a_sum) % 2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == '__main__':
    main()
