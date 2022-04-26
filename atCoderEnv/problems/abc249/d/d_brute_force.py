from sys import stdin
import collections


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A_counter = collections.Counter(A)
    count = 0
    for j, a_j in enumerate(A):
        for k, a_k in enumerate(A):
            count += A_counter[a_k*a_j]
    # for i, a_i in enumerate(A):
    #     for j, a_j in enumerate(A):
    #         q = a_i/a_j
    #         if q.is_integer():
    #             count += A_counter[int(q)]

    print(count)


if __name__ == '__main__':
    main()
