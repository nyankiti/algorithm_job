from sys import stdin


def main():
    N = int(stdin.readline())

    names = []
    for _ in range(N):
        s, t = stdin.readline().split()
        if s in names and t in names:
            print("No")
            return
        names.append(s)
        names.append(t)

    def check():
        for i in range(N):
            if i*2 + 2 >= len(names):
                continue
            if names[i*2] in names[i*2+2:] and names[i*2+1] in names[i*2+2:]:
                return False
        return True

    print("Yes" if check() else "No")


if __name__ == '__main__':
    main()
