from sys import stdin


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    N = int(stdin.readline())
    towns = []
    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        towns.append([x, y])

    magic = {}

    for i in range(N):
        for j in range(i):
            dx = towns[j][0] - towns[i][0]
            dy = towns[j][1] - towns[i][1]
            gcd_val = gcd(dx, dy)
            # print(dx, dy, gcd_val)
            magic[tuple([dx//gcd_val, dy//gcd_val])] = True
            abs_gcd = abs(gcd_val)
            magic[tuple([dx//abs_gcd, dy//abs_gcd])] = True

            dx = towns[i][0] - towns[j][0]
            dy = towns[i][1] - towns[j][1]
            gcd_val = gcd(dx, dy)
            # print(dx, dy, gcd_val)
            magic[tuple([dx//gcd_val, dy//gcd_val])] = True
            abs_gcd = abs(gcd_val)
            magic[tuple([dx//abs_gcd, dy//abs_gcd])] = True

    print(len(magic.values()))


if __name__ == '__main__':
    main()
