#!/usr/bin python
N = int(input())
N_bi = bin(N)[2:]
if len(N_bi) < 31:
    print("Yes")
else:
    print("No")