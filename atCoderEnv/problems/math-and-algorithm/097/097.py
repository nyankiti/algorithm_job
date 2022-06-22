from sys import stdin
import math


def main():
    L, R = map(int, stdin.readline().split())

    is_primes = [True]*(R-L+1)

    if L == 1:
        is_primes[0] = False

    for i in range(2, int(math.sqrt(R))+1):
        min_val = ((L+i-1)//i) * i
        for j in range(min_val, R+1, i):
            if j == i:
                continue
            is_primes[j-L] = False

    print(is_primes.count(True))


if __name__ == '__main__':
    main()
