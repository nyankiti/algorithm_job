from sys import stdin


def main():
    A, B = map(str, stdin.readline().split())

    len_min = min(len(A), len(B))

    for i in range(1, len_min+1):
        if int(A[-i]) + int(B[-i]) >= 10:
            print("Hard")
            break
    else:
        print("Easy")


if __name__ == '__main__':
    main()
