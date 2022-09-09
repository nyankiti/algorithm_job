from collections import Counter
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    diff_num = 0
    c = Counter(S)

    len_keys = len(c.keys())

    if len_keys == 3:
        print(6)
    elif len_keys == 2:
        print(3)
    else:
        print(1)


if __name__ == '__main__':
    main()
