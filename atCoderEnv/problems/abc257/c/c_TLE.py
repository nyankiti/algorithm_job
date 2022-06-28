from sys import stdin


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

    children_wheight.sort(reverse=True)
    parent_wheight.sort()

    # print("child", children_wheight)
    # print("parent", parent_wheight)

    # 末端条件
    if len(parent_wheight) == 0 or len(children_wheight) == 0:
        print(N)
        return

    child_max = children_wheight[0]
    parent_min = parent_wheight[0]

    # 全員を判別できる場合
    if child_max < parent_min:
        print(N)
        return

    def test(x):
        temp_ans = N
        for w in children_wheight:
            if x < w:
                temp_ans -= 1
            else:
                break
        for w in parent_wheight:
            if x > w:
                temp_ans -= 1
            else:
                break
        return temp_ans

    ans = 0
    for i in range(min(len(children_wheight), len(parent_wheight))):
        # 逆を数える場合はindexが一つずれる
        test_1_x = children_wheight[-i-1]-1
        test_2_x = parent_wheight[i]+1
        test_3_x = (children_wheight[-i-1] + parent_wheight[i]) // 2

        ans = max(test(test_1_x), test(test_2_x), test(test_3_x))

    print(ans)


if __name__ == '__main__':
    main()
