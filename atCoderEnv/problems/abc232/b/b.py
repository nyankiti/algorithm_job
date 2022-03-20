from sys import stdin
import string

# print(string.ascii_lowercase)

len_alphabet = len(string.ascii_lowercase)

S = input()
T = input()

diff = []

for i in range(len(S) - 1):
    diff.append((ord(S[i]) - ord(S[i+1])) % len_alphabet)

for i in range(len(T) - 1):
    temp_diff = (ord(T[i]) - ord(T[i+1])) % len_alphabet
    if diff[i] != temp_diff:
        print("No")
        break
else:
    print("Yes")
