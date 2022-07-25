from sys import stdin


def main():

    def get_sub_sequences(string):
        result = []

        def rec(string, substring, pos=0):
            if pos == len(string):
                result.append("".join(substring))
            else:
                # 選ぶ場合
                substring.append(string[pos])
                rec(string, substring, pos + 1)
                # 選ばない場合
                substring.pop()
                rec(string, substring, pos + 1)

        rec(string, [])
        return result

    print(get_sub_sequences("abcd"))


if __name__ == '__main__':
    main()