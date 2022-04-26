from sys import stdin
import collections


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
    *A, = map(int, stdin.readline().split())
    A_counter = collections.Counter(A)
    ans = 0

    for a_i in A_counter.keys():
        divisors = make_divisors(a_i)
        for a_j in divisors:
            a_k = a_i // a_j
            ans += A_counter[a_i] * A_counter[a_j] * A_counter[a_k]

    print(ans)


if __name__ == '__main__':
    main()
