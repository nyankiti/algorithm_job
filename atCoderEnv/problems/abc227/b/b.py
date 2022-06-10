from sys import stdin

"""
4ab + 3a + 3b
"""


def check(s):
    for i in range(1, 1000):
        for j in range(1, 1000):
            if 4*i*j + 3*i + 3*j == s:
                return False
    return True


def main():
    N = int(stdin.readline())
    *S, = map(int, stdin.readline().split())
    ans = 0

    for s in S:
        if check(s):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
