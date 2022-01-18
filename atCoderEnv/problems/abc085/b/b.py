#!/usr/bin python
N = int(input())
motis = []
for _ in range(N):
    motis.append(input())

print(len(set(motis)))