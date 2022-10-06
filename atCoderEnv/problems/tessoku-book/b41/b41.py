from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    X, Y = map(int, stdin.readline().split())
    ans = [[X, Y]]
    while X != 1 or Y != 1:
        if X > Y:
            X = X-Y
        elif Y > X:
            Y = Y - X
        else:
            X = X//2
            Y = X//2
        ans.append([X, Y])
    ans.pop()

    print(len(ans))
    if len(ans) > 0:
        for val in reversed(ans):
            print(*val)


if __name__ == '__main__':
    main()
