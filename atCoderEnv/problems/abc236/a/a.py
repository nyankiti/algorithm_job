from sys import stdin

S = input()
a, b = map(int, stdin.readline().split())

print(S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:])
