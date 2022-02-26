from sys import stdin

target = input()

n = int(stdin.readline())
for _ in range(n):
    pattern = input()
    len_pattern = len(pattern)

    for index, char in enumerate(target):
        if pattern == target[index: index+len_pattern]:
            print(1)
            break
    else:
        print(0)
