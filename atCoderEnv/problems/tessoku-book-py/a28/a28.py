from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    ans = 0
    for _ in range(N):
        T, A = input().split()
        if T == "+":
            ans += int(A)
        elif T == "-":
            ans -= int(A)
        elif T == "*":
            ans *= int(A)
        ans %= 10000
        print(ans)


if __name__ == '__main__':
    main()
