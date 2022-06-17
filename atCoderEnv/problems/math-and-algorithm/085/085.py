from sys import stdin


def main():
    N, X, Y = map(int, stdin.readline().split())
    for a in range(1, N+1):
        for b in range(a, N+1):
            for c in range(b, N+1):
                for d in range(c, N+1):
                    if a+b+c+d == X:
                        if a*b*c*d == Y:
                            print("Yes")
                            return
    print("No")


if __name__ == '__main__':
    main()
