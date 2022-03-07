'''
要素の検索はソートして二分探索！！！
参考：https://twitter.com/e869120/status/1379565222541680644/photo/1
'''

from sys import stdin

N = int(stdin.readline())
A = [-float("inf")] + list(map(int, stdin.readline().split())) + [float("inf")]
A.sort()

Q = int(stdin.readline())

for _ in range(Q):
    b = int(stdin.readline())

    left_index = 0
    right_index = N+1
    while right_index - left_index > 1:
        middle_index = (right_index + left_index) // 2
        if b <= A[middle_index]:
            right_index = middle_index
        else:
            left_index = middle_index

    ans = min(abs(b - A[right_index]), abs(b - A[left_index]))
    print(ans)
