from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    if S == "Monday":
        print(5)
    elif S == "Tuesday":
        print(4)
    elif S == "Wednesday":
        print(3)
    elif S == "Thursday":
        print(2)
    elif S == "Friday":
        print(1)


if __name__ == '__main__':
    main()
