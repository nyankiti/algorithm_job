from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *S, = map(int, stdin.readline().split())
    A = [S[0]]
    for i in range(N-1):
        A.append(S[i+1]-S[i])

    print(*A)


if __name__ == '__main__':
    main()
