from sys import stdin, exit


def main():
    N, W = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    di = {}
    if N == 1:
        if A[0] <= W:
            di[A[0]] = True
        print(len(di.keys()))
        exit()

    if N == 2:
        for i in range(N):
            for j in range(N):
                if i != j:
                    temp_sum = A[i] + A[j]
                    if temp_sum <= W:
                        di[temp_sum] = True
                    temp_sum = A[i]
                    if temp_sum <= W:
                        di[temp_sum] = True
        print(len(di.keys()))
        exit()

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i != j and j != k and i != k:
                    temp_sum = A[i] + A[j] + A[k]
                    if temp_sum <= W:
                        di[temp_sum] = True
                    temp_sum = A[i] + A[j]
                    if temp_sum <= W:
                        di[temp_sum] = True
                    temp_sum = A[j] + A[k]
                    if temp_sum <= W:
                        di[temp_sum] = True
                    temp_sum = A[i] + A[k]
                    if temp_sum <= W:
                        di[temp_sum] = True
                    temp_sum = A[i]
                    if temp_sum <= W:
                        di[temp_sum] = True

    # print(di.keys())
    print(len(di.keys()))


if __name__ == '__main__':
    main()
