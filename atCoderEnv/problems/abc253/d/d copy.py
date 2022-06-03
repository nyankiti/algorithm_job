from sys import stdin

from numpy import number


def main():
    N, A, B = map(int, stdin.readline().split())

    numbers = [True]*N

    temp = A
    i = 2
    while temp < N:
        numbers[temp] = False
        temp = A*i
        i += 1

    temp = B
    i = 2
    while temp < N:
        numbers[temp] = False
        temp = B*i
        i += 1

    ans = 0
    for i, val in enumerate(numbers):
        if val:
            ans += i
    print(numbers)
    print(ans)


if __name__ == '__main__':
    main()
