from sys import stdin

H, W = map(int, stdin.readline().split())

# コーナーケースを考える
if H == 1 or W == 1:
    print(H*W)
else:
    # print(count())
    print(((H+1) // 2) * ((W + 1) // 2))
