from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, H, W = map(int, stdin.readline().split())
    AB = [list(map(int, stdin.readline().split())) for _ in range(N)]

    xor_sum = 0
    for i in range(N):
        xor_sum = xor_sum ^ (AB[i][0] - 1)
    for i in range(N):
        xor_sum = xor_sum ^ (AB[i][1] - 1)
    print("First" if xor_sum != 0 else "Second")


if __name__ == '__main__':
    main()
