from sys import stdin


def main():
    S_1 = input()
    S_2 = input()

    if S_1 == "##" or S_2 == "##":
        print("Yes")
    elif S_1[0] == "#" and S_2[0] == "#":
        print("Yes")
    elif S_1[1] == "#" and S_2[1] == "#":
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
