from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    contests = {"ABC": False, "ARC": False, "AGC": False, "AHC": False}
    S_1 = input()
    S_2 = input()
    S_3 = input()
    contests[S_1] = True
    contests[S_2] = True
    contests[S_3] = True

    for key in contests.keys():
        if contests[key] == False:
            print(key)


if __name__ == '__main__':
    main()
