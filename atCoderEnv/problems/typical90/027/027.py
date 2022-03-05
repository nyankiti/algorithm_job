from sys import stdin

N = int(stdin.readline())

user = {}

for i in range(N):
    user_name = input()
    if user.get(user_name):
        continue
    else:
        user[user_name] = True
        print(i+1)
