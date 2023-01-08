from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    graph = [[] for _ in range(N)]

    for i in range(N):
        if i == N-1:
            graph[i].append(0)
            graph[i].append(1)
        elif i == N-2:
            graph[i].append(i+1)
            graph[i].append(0)
        else:
            graph[i].append(i+1)
            graph[i].append(i+2)

    print(N)
    for val in graph:
        print(val[0]+1, val[1]+1)


if __name__ == '__main__':
    main()
