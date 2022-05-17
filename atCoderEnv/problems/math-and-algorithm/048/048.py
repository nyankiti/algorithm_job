import math
from sys import stdin

"""
むずいから一旦飛ばす (20220515)
"""


def main():
    K = int(stdin.readline())

    ans = math.inf
    for i in range(2, 10*6):
        temp_ans = 0
        for char in str(K*i):
            temp_ans += int(char)
        ans = min(ans, temp_ans)
    print(ans)


if __name__ == '__main__':
    main()
