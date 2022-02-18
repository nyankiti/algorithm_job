from sys import stdin, exit

W, H, x, y, r = map(int, stdin.readline().split())

if x >= r and x <= W-r:
    if y >= r and y <= H-r:
        print("Yes")
        exit()
print("No")
