#!/usr/bin python
N = int(input())
S = input()

result = "0"

for i, char in enumerate(S):
    dest_index = result.find(str(i))
    if char == "L":
        result = result[:i-1] + str(i+1) + result[i-1:]
    elif char == "R":
        result = result[:i] + str(i+1) + result[i:]

# print(" ".join(map(str, a)))
print(result)