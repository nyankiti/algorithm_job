from sys import stdin


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def main():
    A, B = map(int, stdin.readline().split())
    ans = 0
    max_ans = B-A
    for i in range(A, B+1):
        for j in range(i, B+1):
            if i == j:
                continue
            ans = max(ans, gcd(i, j))
            if ans == max_ans:
                break
    print(ans)


if __name__ == '__main__':
    main()
