from sys import stdin

n = int(stdin.readline())

cards = [[False for _ in range(13)] for _ in range(4)]
suits = ["S", "H", "C", "D"]

for _ in range(n):
    mark, num = input().split()
    if mark == "S":
        cards[0][int(num)-1] = True
    elif mark == "H":
        cards[1][int(num)-1] = True
    elif mark == "C":
        cards[2][int(num)-1] = True
    elif mark == "D":
        cards[3][int(num)-1] = True

for i, suit in enumerate(cards):
    for j, elem in enumerate(suit):
        if elem == False:
            print(suits[i], "", end="")
            print(j+1)