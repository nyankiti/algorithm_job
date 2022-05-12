from sys import stdin


def main():
    N, A, B = map(int, stdin.readline().split())
    P, Q, R, S = map(int, stdin.readline().split())

    for i in range(P, Q+1):
        ans = []
        for j in range(R, S+1):
            if (i-j == A-B) or (i+j == A+B):
                ans.append("#")
            else:
                ans.append(".")

        print("".join(ans))


if __name__ == '__main__':
    main()
