from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    visited = {}
    for _ in range(N):
        S = input()
        if S[0] not in ["H", "D", "C", "S"]:
            print("No")
            return
        if S[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
            print("No")
            return
        if S in visited:
            print("No")
            return
        visited[S] = True
    print("Yes")


if __name__ == '__main__':
    main()
