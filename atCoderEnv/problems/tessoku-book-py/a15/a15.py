from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    li = []
    for i, a in enumerate(A):
        li.append([a, i])
    li.sort(key=lambda x: x[0])

    # print(li)
    ans = [0]*N

    prev = -1
    j = 0
    for i in range(N):
        if li[i][0] == prev:
            ans[li[i][1]] = j
        else:
            ans[li[i][1]] = j+1
            j += 1
        prev = li[i][0]
    print(*ans)


if __name__ == '__main__':
    main()
