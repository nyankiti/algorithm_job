from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    state = [False]*(N+1)
    for a in A:
        if a < N+1:
            state[a] = True

    for i in range(N+1):
        for a in A:
            if i - a >= 0 and state[i-a] == False:
                state[i] = True
    print("First" if state[-1] else "Second")


if __name__ == '__main__':
    main()
