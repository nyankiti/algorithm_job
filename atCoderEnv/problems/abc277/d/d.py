from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(lambda x: int(x) % M, stdin.readline().split())
    A.sort()
    # print(A)

    # 連続部分で最も大きい値を探索すれば良い
    ans_list = []
    temp = A[0]
    prev = A[0]
    for i in range(1, N):
        if prev+1 >= A[i]:
            temp += A[i]
        else:
            ans_list.append(temp)
            temp = A[i]
        prev = A[i]
    ans_list.append(temp)

    if len(ans_list) > 1 and A[0] == 0 and A[N-1] == M-1:
        ans_list.append(ans_list[0]+ans_list[-1])
    print(sum(A) - max(ans_list))


if __name__ == '__main__':
    main()
