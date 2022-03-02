from sys import stdin

n = int(stdin.readline())

data = [[[0]*10 for _ in range(3)] for _ in range(4)]

for _ in range(n):
    building_num, floor_num, room_num, people = map(int, input().split())

    data[building_num-1][floor_num-1][room_num-1] += people

for index, building in enumerate(data):
    for floor in building:
        print("",*floor)
    if index != 3:
        print("#"*20)