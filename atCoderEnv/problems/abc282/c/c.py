from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S = input()
    isEnclosed = False
    ans = []
    for i in range(N):
        if S[i] == ',':
            if not isEnclosed:
                ans.append(".")
            else:
                ans.append(",")
        else:
            ans.append(S[i])

        if S[i] == '"':
            isEnclosed = not isEnclosed
    print("".join(ans))


if __name__ == '__main__':
    main()
