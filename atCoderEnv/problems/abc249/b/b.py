from sys import stdin, exit


def main():
    S = input()
    visit_low = False
    visite_up = False
    visited = []
    for char in S:
        if char in visited:
            print("No")
            exit()
        else:
            visited.append(char)
            if char.islower():
                visit_low = True
            if char.isupper():
                visite_up = True
    if visite_up and visit_low:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
