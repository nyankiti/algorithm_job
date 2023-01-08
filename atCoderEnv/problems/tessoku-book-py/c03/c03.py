from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    D = int(stdin.readline())
    X = int(stdin.readline())
    kabuka = [X]
    for _ in range(D-1):
        A = int(stdin.readline())
        kabuka.append(kabuka[-1]+A)

    Q = int(stdin.readline())
    for _ in range(Q):
        S, T = map(lambda x: int(x)-1, stdin.readline().split())
        if kabuka[S] == kabuka[T]:
            print("Same")
        elif kabuka[S] > kabuka[T]:
            print(S+1)
        else:
            print(T+1)


if __name__ == '__main__':
    main()
