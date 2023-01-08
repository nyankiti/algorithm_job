from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    Q = int(stdin.readline())
    di = {}
    for _ in range(Q):
        query = stdin.readline().split()
        if query[0] == "1":
            di[query[1]] = query[2]
        elif query[0] == "2":
            print(di[query[1]])


if __name__ == '__main__':
    main()
