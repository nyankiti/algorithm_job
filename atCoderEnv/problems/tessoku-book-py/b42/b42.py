from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, stdin.readline().split())
        A.append(a)
        B.append(b)

    # 絶対値が最大になる瞬間である4パターンを探索すれば良い
    # Aの表が最大になる場合
    pattern1_A = 0
    pattern1_B = 0
    # Aの裏が最大になる場合
    pattern2_A = 0
    pattern2_B = 0
    # Bの表が最大になる場合
    pattern3_A = 0
    pattern3_B = 0
    # Bの裏が最大になる場合
    pattern4_A = 0
    pattern4_B = 0
    for i in range(N):
        if A[i] + B[i] > 0:
            pattern1_A += A[i]
            pattern1_B += B[i]
        if -A[i]-B[i] > 0:
            pattern2_A += A[i]
            pattern2_B += B[i]
        if A[i] - B[i] > 0:
            pattern3_A += A[i]
            pattern3_B += B[i]
        if -A[i] + B[i] > 0:
            pattern4_A += A[i]
            pattern4_B += B[i]
    print(max(abs(pattern1_A)+abs(pattern1_B), abs(pattern2_A)+abs(pattern2_B),
          abs(pattern3_A)+abs(pattern3_B), abs(pattern4_A)+abs(pattern4_B)))


if __name__ == '__main__':
    main()
