from sys import stdin


def main():
    # atcoderを正しい順番として、転倒数を数えるだけ！
    mapping = {"a": 0, "t": 1, "c": 2, "o": 3, "d": 4, "e": 5, "r": 6}
    S = input()

    # 代わりの数列
    alt_numbers = []

    for char in S:
        alt_numbers.append(mapping[char])

    len_numbers = len(alt_numbers)
    ans = 0
    # バブルソート
    for i in range(len_numbers):
        for j in range(1, len_numbers-i):
            if alt_numbers[j-1] > alt_numbers[j]:
                alt_numbers[j-1], alt_numbers[j] = alt_numbers[j], alt_numbers[j-1]
                ans += 1
    # print(alt_numbers)
    print(ans)


if __name__ == '__main__':
    main()
