from sys import stdin


def main():
    keypad_mapping = {
        "0": "+",
        "1": ".",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
    }

    def keypad_combinations(key):
        result = []

        def rec(
            key,
            combination,
            pos=0,
        ):
            if len(key) == pos:
                result.append("".join(combination))
            else:
                for char in keypad_mapping[key[pos]]:
                    combination.append(char)
                    rec(key, combination, pos + 1)
                    combination.pop()

        rec(key, [])
        return result

    print(keypad_combinations("29"))


if __name__ == '__main__':
    main()