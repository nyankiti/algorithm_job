from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    ans = []
    for num in T:
        if num == "1":
            ans.append(S_1)
        elif num == "2":
            ans.append(S_2)
        else:
            ans.append(S_3)
    print("".join(ans))


if __name__ == '__main__':
    main()
