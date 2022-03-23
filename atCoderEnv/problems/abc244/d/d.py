from sys import stdin

S = input().split()
T = input().split()


if S[0] == T[0] and S[1:] != T[1:]:
    print("No")
elif S[1] == T[1] and S[0] != T[0] and S[2] != T[2]:
    print("No")
elif S[2] == T[2] and S[:2] != T[:2]:
    print("No")
elif S == T:
    print("Yes")
else:
    print("Yes")
