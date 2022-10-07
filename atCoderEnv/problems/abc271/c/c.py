from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    rest_book = deque()

    # 先に重複している漫画をを処理する
    # s = set()
    # dup = []
    # for a in A:
    #     if a in s:
    #         dup.append(a)
    #     else:
    #         rest_book.append(a)
    #         s.add(a)
    # rest_book.extend(dup)

    # 以下のようにすると、setの順番が担保されないことに注意！
    rest_book.extend(sorted(list(set(A))))
    rest_book.extend([-1 for _ in range(N-len(set(A)))])

    next_val = 1
    ans = 0
    while len(rest_book) > 0:
        if next_val == rest_book[0]:
            rest_book.popleft()
            next_val += 1
            ans += 1
        else:
            # 二つ以上残っている時
            if len(rest_book) >= 2:
                ans += 1
                next_val += 1
                rest_book.pop()
                rest_book.pop()
            else:
                break
    print(ans)


if __name__ == '__main__':
    main()
