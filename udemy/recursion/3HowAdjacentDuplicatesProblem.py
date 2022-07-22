from sys import stdin


def main():

    def has_adjacent_duplicates(s, i=0, prev=""):
        if len(s) == i:
            return False
        if s[i] == prev:
            return True
        prev = s[i]
        return has_adjacent_duplicates(s, i + 1, prev)

    print(has_adjacent_duplicates("programming"))
    print(has_adjacent_duplicates("ababa"))


if __name__ == '__main__':
    main()