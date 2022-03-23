from sys import stdin

N = int(stdin.readline())
T = input()

direction = "Right"
point = [0, 0]

for char in T:
    if char == "S":
        if direction == "Right":
            point[0] += 1
        elif direction == "Top":
            point[1] += 1
        elif direction == "Bottom":
            point[1] -= 1
        elif direction == "Left":
            point[0] -= 1
    else:
        if direction == "Right":
            direction = "Bottom"
        elif direction == "Top":
            direction = "Right"
        elif direction == "Bottom":
            direction = "Left"
        elif direction == "Left":
            direction = "Top"

print(*point)
