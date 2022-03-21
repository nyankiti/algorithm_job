"""
円を2倍にすることで列として捉え、累積和を利用する
"""

from sys import stdin

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())

all = sum(A)


def check():
    for i in range(N):
        temp = A[i]
        if temp * 10 == all:
            return True
        for j in range(i+1, N+i):
            temp += A[j % N]
            if temp * 10 == all:
                return True
    return False


print("Yes" if check() else "No")
