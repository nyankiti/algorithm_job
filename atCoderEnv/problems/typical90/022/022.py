from sys import stdin

A, B, C = map(int, stdin.readline().split())


def gcm(x, y):
    if x % y == 0:
        return y
    return gcm(y, x % y)


A_B = gcm(A, B)
B_C = gcm(B, C)
cube_side = gcm(A_B, B_C)


print(A // cube_side + B // cube_side + C // cube_side - 3)
