from sys import stdin


def main():
    N, Q = map(int, stdin.readline().split())
    kaisa = [0]*N
    for _ in range(Q):
        L, R, X = map(int, stdin.readline().split())
        kaisa[L-1] += X
        if R < N:
            kaisa[R] -= X
    # print(kaisa)

    for i in range(1, N):
        if kaisa[i] < 0:
            print(">", end="")
        elif kaisa[i] > 0:
            print("<", end="")
        else:
            print("=", end="")
    print()

    # cumlateive_sum = []
    # temp_sum = 0
    # for num in kaisa:
    #     temp_sum += num
    #     cumlateive_sum.append(temp_sum)
    # print(cumlateive_sum)


if __name__ == '__main__':
    main()
