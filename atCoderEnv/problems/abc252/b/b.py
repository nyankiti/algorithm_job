from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    max_a = max(A)
    li = []
    for index, a in enumerate(A):
        if a == max_a:
            li.append(index+1)

    for b in B:
        if b in li:
            print("Yes")
            break
    else:
        print("No")


if __name__ == '__main__':
    main()
