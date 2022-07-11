from sys import stdin


def shorten_str(string):
    new_S = []
    count_li = []
    prev_char = ""
    count = 1
    for char in string:
        if prev_char == char:
            count += 1
        else:
            if count >= 2:
                new_S.append(prev_char)
                new_S.append(prev_char)
            else:
                new_S.append(prev_char)
            count_li.append(count)
            count = 1

        prev_char = char

    if count >= 2:
        new_S.append(char)
        new_S.append(char)
    else:
        new_S.append(char)
    count_li.append(count)

    return "".join(new_S), count_li[1:]


def main():
    S = input()
    T = input()

    # 同じ連続する箇所でも、Sの方が長い場合はアウト

    # 互いの文字の3つ以上連続している箇所を2つに置き換える
    new_S, S_count_li = shorten_str(S)
    new_T, T_count_li = shorten_str(T)

    # print(new_S, S_count_li)
    # print(new_T, T_count_li)

    flg = True
    for i in range(min(len(S_count_li), len(T_count_li))):
        if S_count_li[i] > T_count_li[i]:
            flg = False
            break

    if new_S == new_T and flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
