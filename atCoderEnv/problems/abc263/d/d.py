from sys import stdin


def main():
    N, L, R = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    A_sum = sum(A)

    left_flg = True

    right_flg = True

    right_count = 0
    left_count = 0
    for i in range(N//2+1):
        if left_flg == False and right_flg == False:
            break
        # 左右の両側から侵食する
        if left_flg and A[i] >= L:
            A_sum -= A[i]
            A_sum += L
        else:
            left_flg = False

        if right_flg and A[N-1 - i] >= R:
            A_sum -= A[N-1-i]
            A_sum += R
        else:
            right_flg = False

        right_count += 1
        left_count += 1

    left_test_sum = A_sum
    # 左側を限界まで侵食する場合
    left_test_sum -= A[left_count-1]
    left_test_sum += L
    while left_count < N:
        # print(A[left_count], L)
        if A[left_count] >= L:
            left_test_sum -= A[left_count]
            left_test_sum += L
            left_count += 1
        else:
            break

    right_test_sum = A_sum
    right_count -= 1
    # 右側を限界まで侵食する場合
    while right_count < N:
        # print(right_count)
        # print(right_test_sum)
        if A[N - 1 - right_count] >= R:
            right_test_sum -= A[N-1-right_count]
            right_test_sum += R
            right_count += 1
        else:
            break

    # print(A_sum, left_test_sum, right_test_sum)
    print(min(A_sum, left_test_sum, right_test_sum))


if __name__ == '__main__':
    main()
