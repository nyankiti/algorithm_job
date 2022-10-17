from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    even = []
    odd = []
    for a in A:
        if a % 2 == 0:
            even.append(a)
        else:
            odd.append(a)
    even.sort(reverse=True)
    odd.sort(reverse=True)

    ans = -1
    if len(even) > 1:
        ans = max(ans, even[0]+even[1])
    if len(odd) > 1:
        ans = max(ans, odd[0]+odd[1])
    print(ans)


if __name__ == '__main__':
    main()
