from sys import stdin


def main():
    S = input()
    counter = {}
    for c in S:
        counter[c] = counter.get(c, 0) + 1

    # print(counter)
    for key, val in counter.items():
        if val == 1:
            print(key)
            break
    else:
        print(-1)


if __name__ == '__main__':
    main()
