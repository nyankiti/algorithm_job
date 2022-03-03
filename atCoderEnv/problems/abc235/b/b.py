from sys import stdin

N = int(input())
stands = list(map(int, input().split()))
result = 0
len_stansd = len(stands)

if result < stands[0]:
    result = stands[0]

for index, height in enumerate(stands):

    if index <= len_stansd-2:
        if result < stands[index+1]:
            result = stands[index+1]
        else:
            break

print(result)
