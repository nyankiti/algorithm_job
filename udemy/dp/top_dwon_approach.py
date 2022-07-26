from sys import stdin


def main():

    def fib(n, lookup=None):
        lookup = {} if lookup is None else lookup

        if n in lookup:
            return lookup[n]

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup)
            return lookup[n]


if __name__ == '__main__':
    main()