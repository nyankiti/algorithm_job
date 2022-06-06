from sys import stdin


def main():
    N = int(stdin.readline())
    ans = []
    temp = []
    for i in range(N):
        ans.append([1]*(i+1))
        temp.append([1]*(i+1))

    for i, A in enumerate(temp):
        for j in range(len(A)):
            if (j == 0 or i == j):
                ans[i][j] = 1
            else:
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

    for row in ans:
        print(*row)


if __name__ == '__main__':
    main()
