from sys import stdin

target = input()
pattern = input()

len_pattern = len(pattern)

for index, char in enumerate(target):
    if pattern == target[index: index+len_pattern]:
        print(index)
