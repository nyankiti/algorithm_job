from sys import stdin


def main():

    def reverse(s, i=0, result=""):
        if len(s) == i:
            return result

        result += s[len(s) - i - 1]

        return reverse(s, i + 1, result)

    print(reverse("abcd"))
    print(reverse("inside code"))

    # 分割統治で書く方法
    def reverse_divide_conquer(s):
        if len(s) <= 1:
            return s
        else:
            mid = len(s) // 2
            left_part = s[:mid]
            right_part = s[mid:]
            return reverse_divide_conquer(right_part) + reverse_divide_conquer(
                left_part)

    print(reverse_divide_conquer("abcd"))
    print(reverse_divide_conquer("inside code"))


if __name__ == '__main__':
    main()