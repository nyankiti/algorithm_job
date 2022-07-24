from sys import stdin, exit


def main():
    N = int(stdin.readline())
    result = []
    for _ in range(N):
        *A, = list(input())
        result.append(A)

    # for row in result:
    #     print(row)

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            # print(result[i][j])
            # print(result[N-i-1][N-j-1])
            # print("----------------------")
            if result[i][j] == "W":
                if result[N-i-1][N-j-1] != "L":
                    print("incorrect")
                    exit()
            elif result[i][j] == "L":
                if result[N-i-1][N-j-1] != "W":
                    print("incorrect")
                    exit()
            elif result[i][j] == "D":
                if result[N-i-1][N-j-1] != "D":
                    print("incorrect")
                    exit()
    else:
        print("correct")


if __name__ == '__main__':
    main()
