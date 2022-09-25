from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    X, Y, Z = map(int, stdin.readline().split())

    ans = []
    # 全て正数
    if X > 0 and Y > 0 and Z > 0:
        # 直接行けるパターン
        if X < Y:
            # print(X)
            ans.append(X)
        # ハンマーで行けるパターン
        elif Z < Y:
            # print(X)
            ans.append(X)
        # else:
        #     print(-1)
    # 全て負数
    elif X < 0 and Y < 0 and Z < 0:
        X, Y, Z = abs(X), abs(Y), abs(Z)
        # 直接行けるパターン
        if X < Y:
            # print(X)
            ans.append(X)
        # ハンマーで行けるパターン
        elif Z < Y:
            ans.append(X)
            # print(X)
        # else:
        #     print(-1)
    else:
        # 直接行けるパターン(壁の内側にゴール)
        if abs(X) < abs(Y):
            ans.append(abs(X))
            # print(abs(X))
        # 直接行けるパターン(逆向きにゴール)
        elif (X > 0 and Y < 0) or (X < 0 and Y > 0):
            ans.append(abs(X))
            # print(abs(X))
        # ハンマーを拾ってゴールできるパターン(ハンマーが内側にある)
        elif abs(Z) < abs(Y):
            ans.append(abs(Z) + abs(X-Z))
            # print(abs(Z) + abs(X-Z))
        # ハンマーを拾ってゴールできるパターン(ハンマーが逆方向にある)
        elif (Z > 0 and Y < 0) or (Z < 0 and Y > 0):
            ans.append(abs(Z) + abs(X-Z))
            # print(abs(Z) + abs(X-Z))
        # else:
        #     print(-1)
    if len(ans) == 0:
        print(-1)
    else:
        print(min(ans))


if __name__ == '__main__':
    main()
