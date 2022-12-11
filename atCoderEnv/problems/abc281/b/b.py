from sys import stdin, setrecursionlimit
import string

setrecursionlimit(10**6)


def main():
    upper_alphabet = string.ascii_uppercase
    S = input()

    if len(S) == 8:
        if S[0] in upper_alphabet:
            if S[1:7].isdecimal():
                if 100000 <= int(S[1:7]) and int(S[1:7]) <= 999999:
                    if S[7:8] in upper_alphabet:
                        print("Yes")
                        return
    print("No")


if __name__ == '__main__':
    main()
