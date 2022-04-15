from sys import stdin


def main():
    def cross(a_x, a_y, b_x, b_y):
        return a_x*b_y - a_y*b_x

    x_1, y_1 = map(int, stdin.readline().split())  # A
    x_2, y_2 = map(int, stdin.readline().split())  # B
    x_3, y_3 = map(int, stdin.readline().split())  # C
    x_4, y_4 = map(int, stdin.readline().split())  # D

    AC = (x_3-x_1, y_3-y_1)
    AB = (x_2-x_1, y_2-y_1)
    AD = (x_4-x_1, y_4-y_1)
    CA = (x_1-x_3, y_1-y_3)
    CB = (x_2-x_3, y_2-y_3)
    CD = (x_4-x_3, y_4-y_3)

    AB_AC_cross = cross(AB[0], AB[1], AC[0], AC[1])
    AB_AD_cross = cross(AB[0], AB[1], AD[0], AD[1])
    CD_CA_cross = cross(CD[0], CD[1], CA[0], CA[1])
    CD_CB_cross = cross(CD[0], CD[1], CB[0], CB[1])
    # コーナーケース(一直線に並ぶ場合)
    if AB_AC_cross == 0 and AB_AD_cross == 0 and CD_CA_cross == 0 and CD_CB_cross == 0:
        A = (x_1, y_1)
        B = (x_2, y_2)
        C = (x_3, y_3)
        D = (x_4, y_4)

        if A > B:
            A, B = B, A
        if C > D:
            C, D = D, C

        if max(A, C) <= min(B, D):
            print("Yes")
        else:
            print("No")
        return

    # 直線ABが点C,Dを分ける。かつ、直線CDが点A,Bを分ける。が成り立てば二つの線分は交差する
    if (AB_AC_cross >= 0 and AB_AD_cross <= 0) or (AB_AC_cross <= 0 and AB_AD_cross >= 0):
        if (CD_CA_cross >= 0 and CD_CB_cross <= 0) or (CD_CA_cross >= 0 and CD_CB_cross <= 0):
            print("Yes")
            return

    print("No")

    # 直線ABが点C,Dを分ける。かつ、直線CDが点A,Bを分ける。が成り立てば二つの線分は交差する
    # if AB_AC_cross * AB_AD_cross < 0 and CD_CA_cross * CD_CB_cross <= 0:
    #     print("Yes")
    # elif AB_AC_cross * AB_AD_cross > 0 and CD_CA_cross * CD_CB_cross >= 0:
    #     print("Yes")
    # else:
    #     print("No")


if __name__ == '__main__':
    main()
