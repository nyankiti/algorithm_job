from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A.sort()
    ans = []
    rest_book = deque()
    rest_book.extend(A)

    if N == 1:
        if A[0] == 1:
            print(1)
        else:
            print(0)
        return

    if A[0] != 1:
        ans.append(1)
        rest_book.pop()
        rest_book.pop()
    else:
        ans.append(A[0])
        rest_book.popleft()

    while rest_book:
        if ans[-1] + 1 == rest_book[0]:
            ans.append(rest_book.popleft())
        else:
            # 二つ以上残っている時
            if len(rest_book) >= 2:
                ans.append(ans[-1]+1)
                rest_book.pop()
                rest_book.pop()
            else:
                break
    print(len(ans))


if __name__ == '__main__':
    main()
