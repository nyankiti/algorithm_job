from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    prime_table = [True]*300001
    for i in range(2, 300001):
        j = i
        if prime_table[i] == True:
            j += i
        while j <= 300000:
            prime_table[j] = False
            j += i

    Q = int(stdin.readline())
    for _ in range(Q):
        X = int(stdin.readline())
        print("Yes" if prime_table[X] else "No")


if __name__ == '__main__':
    main()
