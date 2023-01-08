import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    r_start, c_start = map(int, stdin.readline().split())
    r_goal, c_goal = map(int, stdin.readline().split())
    r_start, c_start = r_start-1, c_start-1
    r_goal, c_goal = r_goal-1, c_goal-1

    maze = []
    for _ in range(H):
        S = input()
        maze.append(list(S))


if __name__ == '__main__':
    main()
