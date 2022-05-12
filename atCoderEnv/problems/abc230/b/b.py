from sys import stdin


def main():
    S = input()
    len_S = len(S)
    T = "oxx" * 10**5
    for i in range(0, int(len(T)/len_S)):
        if S == T[i:i+len_S]:
            print("Yes")
            break
    else:
        print("No")


if __name__ == '__main__':
    main()
