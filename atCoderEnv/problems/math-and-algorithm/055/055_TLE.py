from sys import stdin

"""
a_1=1,a_2=1
a_n= 2 * a_{n－1} + a_{n－2} (n≥3)
"""


def f(n, memo):
    if memo.get(n):
        return memo[n]

    if n == 1 or n == 2:
        return 1
    ans = 2*f(n-1, memo) + f(n-2, memo)
    memo[n] = ans
    return ans


def main():
    N = int(stdin.readline())
    memo = {}
    print(f(N, memo))


if __name__ == '__main__':
    main()
