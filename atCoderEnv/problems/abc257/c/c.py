from sys import stdin
import bisect


def main():
    N = int(stdin.readline())
    S = input()
    *W, = map(int, stdin.readline().split())

    children_wheight = []
    parent_wheight = []
    for i, s in enumerate(S):
        if s == "1":
            parent_wheight.append(W[i])
        elif s == "0":
            children_wheight.append(W[i])

    children_wheight.sort()
    parent_wheight.sort()

    # 末端条件
    if len(parent_wheight) == 0 or len(children_wheight) == 0:
        print(N)
        return

    child_max = children_wheight[-1]
    parent_min = parent_wheight[0]

    # 全員を判別できる場合
    if child_max < parent_min:
        print(N)
        return

    len_chiled = len(children_wheight)
    len_parent = len(parent_wheight)

    def test(x):
        temp_ans = N
        chi = bisect.bisect_right(children_wheight, x)
        pa = bisect.bisect_right(parent_wheight, x)

        if chi != len_chiled and x == children_wheight[chi]:
            # print("child", x)
            temp_ans -= (len_chiled-chi-2)
        else:
            # print("if not child", x)
            temp_ans -= (len_chiled-chi-1)

        if pa != len_parent and x == parent_wheight[pa]:
            # print("parent", x)
            temp_ans -= pa+2
        else:
            # print("if not parent", x)
            temp_ans -= (pa+1)
        # print("temo ans", temp_ans)
        return temp_ans

    ans = 0
    for i in range(min(len(children_wheight), len(parent_wheight))):
        # 逆を数える場合はindexが一つずれる
        test_1_x = children_wheight[-i-1]-1
        test_2_x = parent_wheight[i]+1
        test_3_x = (children_wheight[-i-1] + parent_wheight[i]) // 2 + 1
        test_4_x = (children_wheight[-i-1] + parent_wheight[i]) // 2 - 1
        test_5_x = (children_wheight[-i-1] + parent_wheight[i]) // 2
        test_6_x = children_wheight[-i-1]
        test_7_x = parent_wheight[i]

        test_8_x = children_wheight[-i-1]+1
        test_9_x = parent_wheight[i]-1

        ans = max(test(test_1_x), test(test_2_x), test(
            test_3_x), test(test_4_x), test(test_5_x), test(test_6_x), test(test_7_x), test(test_8_x), test(test_9_x), ans)

    print(ans)


if __name__ == '__main__':
    main()
