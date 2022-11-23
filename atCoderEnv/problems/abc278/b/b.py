from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    def check(H, M):
        if len(H) == 1:
            H = "0"+H
        if len(M) == 1:
            M = "0"+M

        A, B = list(H)
        C, D = list(M)

        # 右上と左下を入れ替え
        B, C = C, B

        H = int(A+B)
        M = int(C+D)
        # もし、H, Mが時間として成立する場合は、True
        if 0 <= H and H <= 23 and 0 <= M and M <= 59:
            return True
        else:
            return False

    H, M = map(int, stdin.readline().split())

    while True:
        if check(str(H), str(M)):
            print(H, M)
            return

        if M == 59:
            M = 0
            if H == 23:
                H = 0
            else:
                H += 1
        else:
            M += 1


if __name__ == '__main__':
    main()
