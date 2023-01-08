from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    A, B = map(int, stdin.readline().split())
    for i in range(A, B+1):
        if 100 % i == 0:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
