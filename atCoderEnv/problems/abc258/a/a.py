from sys import stdin


def main():
    K = int(stdin.readline())
    hour = 21

    if K >= 60:
        hour += 1
        K -= 60

    if K < 10:
        minute = "0"+str(K)
    else:
        minute = str(K)

    print(str(hour) + ":" + str(minute))


if __name__ == '__main__':
    main()
