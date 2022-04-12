from sys import stdin, exit


def main():
    N = int(stdin.readline())

    names = []
    each_names = []
    for _ in range(N):
        full_name = tuple(stdin.readline().split())
        if full_name in names:
            print("No")
            exit()
        names.append(full_name)
        each_names.append(full_name[0])
        each_names.append(full_name[1])

    def check():
        for i in range(2**N):
            temp = []
            for j in range(N):
                if ((i >> j) & 1):
                    if names[j][0] in temp or names[j][0] in each_names[j*2:]:
                        break
                    temp.append(names[j][0])
                else:
                    if names[j][1] in temp or names[j][1] in each_names[j*2:]:
                        break
                    temp.append(names[j][1])
            else:
                return True

        return False
    # print("Yes" if check() else "No")
    if check():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
