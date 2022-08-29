import math
from sys import stdin


def get_kaku_ABC(A_x, A_y, B_x, B_y, C_x, C_y):
    vec_BA = (A_x - B_x, A_y - B_y)
    vec_BC = (C_x - B_x, C_y - B_y)
    abs_BA = math.sqrt((A_x - B_x)**2 + (A_y - B_y)**2)
    abs_BC = math.sqrt((C_x - B_x)**2 + (C_y - B_y)**2)
    naiseki = (vec_BA[0] * vec_BC[0]) + (vec_BA[1] * vec_BC[1])
    cosBAC = naiseki/(abs_BA*abs_BC)
    return math.degrees(math.acos(cosBAC))


def main():
    A_x, A_y = map(int, stdin.readline().split())
    B_x, B_y = map(int, stdin.readline().split())
    C_x, C_y = map(int, stdin.readline().split())
    D_x, D_y = map(int, stdin.readline().split())

    kakuABC = get_kaku_ABC(A_x, A_y, B_x, B_y, C_x, C_y)
    kakuBCD = get_kaku_ABC(B_x, B_y, C_x, C_y, D_x, D_y)
    kakuCDA = get_kaku_ABC(C_x, C_y, D_x, D_y, A_x, A_y)
    kakuDAB = get_kaku_ABC(D_x, D_y, A_x, A_y, B_x, B_y)
    # print(kakuABC)
    # print(kakuBCD)
    # print(kakuCDA)
    # print(kakuDAB)
    interior_angles_sum = kakuABC + kakuBCD + kakuCDA + kakuDAB
    interior_angles_sum = round(interior_angles_sum)
    if interior_angles_sum < 360:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
