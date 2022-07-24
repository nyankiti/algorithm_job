from sys import stdin, exit


def main():
    L_1, R_1, L_2, R_2 = map(int, stdin.readline().split())

    line = [0]*100
    for i in range(L_1, R_1):
        line[i] += 1
    for j in range(L_2, R_2):
        line[j] += 1

    ans = 0
    for val in line:
        if val == 2:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
