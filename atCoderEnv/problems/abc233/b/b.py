from sys import stdin

L, R = map(int, stdin.readline().split())
S = list(input())
rev = list(reversed(S[L-1:R]))
ans = S[:L-1] + rev + S[R:]

print("".join(ans))
