from sys import stdin


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    N = int(stdin.readline())
    ans = 0
    for i in range(1, N+1):
        ans += (i * len(make_divisors(i)))
    print(ans)


if __name__ == '__main__':
    main()
