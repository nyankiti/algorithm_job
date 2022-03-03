from sys import stdin
from collections import Counter

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())

counter = Counter(A)

for key in counter:
    if counter[key] == 3:
        print(key)
