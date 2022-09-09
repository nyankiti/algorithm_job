from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    T = input()
    new_T = list(T)
    len_S = len(S)

    for i in range(len_S):
        if S[i] != T[i] and i+1 < len_S:
            new_T[i], new_T[i+1] = new_T[i+1], new_T[i]
            break

    print("Yes" if S == "".join(new_T) else "No")


if __name__ == '__main__':
    main()
