from collections import defaultdict
import sys


N, Q = tuple(map(int, input().split(" ")))
numbers = list(map(int, input().split(" ")))

number_pairs = []

for input in sys.stdin:
    number_pairs.append(tuple(map(int, input.split(" "))))

# print(N)
# print(Q)
# print(numbers)
# print(number_pairs)

visited = defaultdict(lambda: 0)
result = [-1] * Q

for num_idx, num in enumerate(numbers):
    for pair_idx, pair in enumerate(number_pairs):
        if pair[0] == num:
            visited[pair] += 1
            if visited[pair] == pair[1]:
                # print("一致したよ"+str(visited))
                result[pair_idx] = num_idx+1

for elem in result:
    print(elem)
