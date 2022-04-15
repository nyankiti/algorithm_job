from sys import stdin
import math


def main():
    a_x, a_y = map(int, stdin.readline().split())
    b_x, b_y = map(int, stdin.readline().split())
    c_x, c_y = map(int, stdin.readline().split())

    BA_vec = (a_x-b_x, a_y-b_y)
    BC_vec = (c_x-b_x, c_y-b_y)
    CA_vec = (a_x-c_x, a_y-c_y)
    CB_vec = (b_x-c_x, b_y-c_y)

    if (BA_vec[0] * BC_vec[0] + BA_vec[1] * BC_vec[1] < 0):
        # pattern = 1
        BA_distance = math.sqrt(BA_vec[0]*BA_vec[0] + BA_vec[1]*BA_vec[1])
        print("%.12f" % BA_distance)
    elif (CA_vec[0] * CB_vec[0] + CA_vec[1] * CB_vec[1] < 0):
        # pattern = 3
        CA_distance = math.sqrt(CA_vec[0]*CA_vec[0] + CA_vec[1]*CA_vec[1])
        print("%.12f" % CA_distance)
    else:
        # pattern = 2
        gaiseki = abs(BA_vec[0]*BC_vec[1] - BA_vec[1]*BC_vec[0])
        BC_distance = math.sqrt(BC_vec[0]*BC_vec[0] + BC_vec[1]*BC_vec[1])

        ans = gaiseki / BC_distance
        print("%.12f" % ans)


if __name__ == '__main__':
    main()
