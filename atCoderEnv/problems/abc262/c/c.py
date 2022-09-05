from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    # brute force(TLE)
    # ans = 0
    # for i in range(N):
    #     for j in range(i+1, N):
    #         if min(A[i], A[j]) == i+1 and max(A[i], A[j]) == j+1:
    #             print(A[i], A[j])
    #             ans += 1

    # print(ans)

    ans = 0
    same = []

    for i in range(N):
        if A[i] == i+1:
            same.append(A[i])
        else:
            if i+1 == A[A[i]-1]:
                # print(A[i], A[A[i]-1])
                ans += 1
    ans //= 2

    ans += len(same) * (len(same)-1) // 2
    print(ans)


if __name__ == '__main__':
    main()
