from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    friend_count = [0]*N
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        friend_count[A-1] += 1
        friend_count[B-1] += 1
    max_val = max(friend_count)
    print(friend_count.index(max_val)+1)


if __name__ == '__main__':
    main()
