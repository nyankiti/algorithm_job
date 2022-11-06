from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    for i in range(len(S)-1, -1, -1):
        if S[i] == "a":
            print(i+1)
            break
    else:
        print(-1)


if __name__ == '__main__':
    main()
