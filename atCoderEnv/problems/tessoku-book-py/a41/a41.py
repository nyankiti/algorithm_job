from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S = list(input())
    prev_color = "W"
    streak = 1
    for s in S:
        if s == prev_color:
            streak += 1
            if streak == 3:
                print("Yes")
                return
        else:
            prev_color = s
            streak = 1
    print("No")


if __name__ == '__main__':
    main()
