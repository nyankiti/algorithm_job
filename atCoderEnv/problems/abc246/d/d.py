from sys import stdin, exit
import math

N = int(stdin.readline())


root_N = math.ceil(N ** (1/3))
# print(root_N)
if root_N > 0:
    for i in range(root_N, N+1):
        for j in range(i+1):
            ans = (i + j)*(i**2 + j**2)
            if ans >= N:
                print(ans)
                exit()
else:
    for i in range(N+1):
        for j in range(i+1):
            ans = (i + j)*(i**2 + j**2)
            if ans >= N:
                print(ans)
                exit()
