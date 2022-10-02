from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, X, Y = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    grundy = [0]*100001
    for i in range(1, 100001):
        temp = []
        if i-X >= 0:
            temp.append(grundy[i-X])
        if i-Y >= 0:
            temp.append(grundy[i-Y])

        for j in range(10):
            if j not in temp:
                grundy[i] = j
                break
    xor_sum = 0
    for a in A:
        xor_sum ^= grundy[a]
    print("First" if xor_sum != 0 else "Second")


if __name__ == '__main__':
    main()
