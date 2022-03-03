from sys import stdin

K = int(stdin.readline())


def base10int(value, base):
    if (value // base):
        return base10int((value // base), base) + str(value % base)
    return str(value % base)


binary = base10int(K, 2)
print(binary.replace("1", "2"))
