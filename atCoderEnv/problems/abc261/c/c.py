from sys import stdin


def main():
    N = int(stdin.readline())
    counter = {}
    for _ in range(N):
        S = input()
        cnt = counter.get(S, 0)
        if cnt == 0:
            print(S)
        else:
            print(S + "(" + str(cnt) + ")")
        counter[S] = cnt+1


if __name__ == '__main__':
    main()
