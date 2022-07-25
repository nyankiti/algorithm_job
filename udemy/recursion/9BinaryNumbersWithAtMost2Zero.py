from sys import stdin


def main():

    def binary_numbers(n):
        result = []

        def rec(n, pos, bin, zero_count):
            if zero_count > 2:
                return

            if n == pos:
                result.append("".join(bin))
            else:
                bin.append("0")
                rec(n, pos + 1, bin, zero_count + 1)
                bin.pop()
                bin.append("1")
                rec(n, pos + 1, bin, zero_count)
                bin.pop()

        rec(n, 0, [], 0)
        return result

    print(binary_numbers(4))


if __name__ == '__main__':
    main()