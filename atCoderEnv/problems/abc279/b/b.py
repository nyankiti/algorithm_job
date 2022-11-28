from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    T = input()
    len_T = len(T)
    for i in range(len(S)-len_T+1):
        if S[i:i+len_T] == T:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
