from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    first_half_A = A[:N//2]
    first_half = []
    second_half_A = A[N//2:]
    second_half_dict = defaultdict(bool)

    # それぞれをbit全探索して組み合わせを求める
    for i in range(2 ** len(first_half_A)):
        temp = 0
        for j in range(len(first_half_A)):
            if ((i >> j) & 1):
                temp += first_half_A[j]
        first_half.append(temp)

    for i in range(2 ** len(second_half_A)):
        temp = 0
        for j in range(len(second_half_A)):
            if ((i >> j) & 1):
                temp += second_half_A[j]
        second_half_dict[temp] = True

    for val in first_half:
        if second_half_dict[K-val]:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
