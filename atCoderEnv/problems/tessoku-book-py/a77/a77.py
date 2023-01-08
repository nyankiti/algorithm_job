from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, L = map(int, stdin.readline().split())
    K = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    def check(x):
        count, last_kireme = 0, 0
        for i in range(N):
            if A[i] - last_kireme >= x and L - A[i] >= x:
                count += 1
                last_kireme = A[i]
        if count >= K:
            return True
        else:
            return False

    left = 0
    right = 1000000000
    while left < right:
        mid = (left+right+1)//2
        ans = check(mid)
        if ans == False:
            right = mid - 1
        else:
            left = mid

    print(left)


if __name__ == '__main__':
    main()
