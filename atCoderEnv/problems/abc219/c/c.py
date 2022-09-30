from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    X = input()
    # 番号を割り振る
    basic_alphabet = "abcdefghijklmnopqrstuvwxyz"
    # 新しいアルファベットを元のアルファベットに変換数
    new_order_map = {}
    old_order_map = {}
    for i, char in enumerate(X):
        new_order_map[char] = basic_alphabet[i]
        old_order_map[basic_alphabet[i]] = char

    N = int(stdin.readline())

    strings = [input() for _ in range(N)]

    converted_strings = []
    for s in strings:
        temp = []
        for char in s:
            temp.append(new_order_map[char])
        converted_strings.append("".join(temp))

    converted_strings.sort()

    for s in converted_strings:
        temp = []
        for char in s:
            temp.append(old_order_map[char])
        print("".join(temp))


if __name__ == '__main__':
    main()
