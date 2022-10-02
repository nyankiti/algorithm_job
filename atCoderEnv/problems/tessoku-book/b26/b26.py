from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    prime_table = [True]*(N+1)
    for i in range(2, N+1):
        j = i
        if prime_table[i] == True:
            print(i)
            j += i
        while j <= N:
            prime_table[j] = False
            j += i


if __name__ == '__main__':
    main()
