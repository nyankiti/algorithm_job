import math

N = int(input())

coordinates = []
while True:
    try:
        coordinates.append(list(map(int, input().split(' '))))
    except EOFError:
        break


def getDistance(point1, point2):
    delta_x = abs(point1[0] - point2[0])
    delta_y = abs(point1[1] - point2[1])
    return math.sqrt(delta_x**2 + delta_y**2)


min_distance = -math.inf
len_coordinates = len(coordinates)

for i in range(len_coordinates):
    for j in range(i, len_coordinates):
        min_distance = max(min_distance, getDistance(
            coordinates[i], coordinates[j]))

print(min_distance)
