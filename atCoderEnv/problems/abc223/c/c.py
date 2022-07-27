from sys import stdin


def main():
    N = int(stdin.readline())
    doukasens = []
    t = 0
    for _ in range(N):
        A, B = map(int, stdin.readline().split())
        doukasens.append([A, B])
        t += A/B
    t /= 2

    # 時刻 t において、導火線がどこにあるかをシミュレーションする
    distance = 0
    for a, b in doukasens:
        if t > a/b:
            t -= a/b
            distance += a
        else:
            distance += b*t
            t -= t

    print("%.15f" % distance)


if __name__ == '__main__':
    main()
