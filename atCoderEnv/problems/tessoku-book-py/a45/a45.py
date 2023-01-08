from collections import Counter
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, color = stdin.readline().split()
    N = int(N)
    A = input()
    c = Counter(A)
    score = 0
    score += c["W"]*0
    score += c["B"]*1
    score += c["R"]*2

    if score % 3 == 0 and color == "W":
        print("Yes")
    elif score % 3 == 1 and color == "B":
        print("Yes")
    elif score % 3 == 2 and color == "R":
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
