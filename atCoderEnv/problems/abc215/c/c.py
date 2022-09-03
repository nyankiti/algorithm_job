from sys import stdin
import itertools


def main():
    inp = stdin.readline().split()
    S = inp[0]
    K = int(inp[1])
    S_li = list(S)
    S_li.sort()

    visited = {}
    count = 0

    for perm in itertools.permutations(S_li):
        if perm not in visited:
            visited[perm] = True
            count += 1

            if count == K:
                print("".join(perm))


if __name__ == '__main__':
    main()
