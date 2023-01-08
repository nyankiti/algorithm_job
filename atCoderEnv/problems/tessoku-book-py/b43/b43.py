from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    # 生徒 i の 不正解数をカウントする
    students = [0]*N
    for a in A:
        students[a-1] += 1
    for val in students:
        print(M-val)


if __name__ == '__main__':
    main()
