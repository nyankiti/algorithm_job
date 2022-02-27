from sys import stdin
import re

target = input()

n = int(stdin.readline())

# for _ in range(n):
#     pattern = input()
#     len_pattern = len(pattern)

#     for index, char in enumerate(target):
#         if pattern == target[index: index+len_pattern]:
#             print(1)
#             break
#     else:
#         print(0)


# 正規表現を用いてTLEしてしまう、、、
for _ in range(n):
    pattern = input()
    regex = re.compile(pattern)

    result = regex.search(target)
    if result:
        print(1)
    else:
        print(0)
