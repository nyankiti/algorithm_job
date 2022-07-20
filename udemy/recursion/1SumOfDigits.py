from sys import stdin


def main():

    def sum_of_digits(n):
        if n < 10:
            return n
        return n % 10 + sum_of_digits(n // 10)

    # 以下のように書くと space complexityが減るので良い。
    def sum_of_digits_2(n, sum=0):
        if n < 10:
            return n + sum
        return sum_of_digits_2(n // 10, n % 10 + sum)

    print(sum_of_digits_2(234))


if __name__ == '__main__':
    main()