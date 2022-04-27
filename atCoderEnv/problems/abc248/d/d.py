from sys import stdin
import ast


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    Q = int(stdin.readline())
    # 和をメモしておいて、引き算するだけにすれば良い
    sum_array = ["{}".format({})]
    counter = {}
    for i in range(N):
        a = A[i]
        counter[a] = counter.get(a, 0) + 1
        str_counter = "{}".format(counter)
        sum_array.append(str_counter)

    # print(sum_array)
    for _ in range(Q):
        L, R, X = map(int, stdin.readline().split())

        ans = ast.literal_eval(sum_array[R]).get(
            X, 0) - ast.literal_eval(sum_array[L-1]).get(X, 0)
        print(ans)


if __name__ == '__main__':
    main()
