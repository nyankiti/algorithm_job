x, y = map(int, input().split())

# ユーグリットの互除法を使う


def euclidean_algorithm(x, y):
    r = x % y
    if r == 0:
        return y
    else:
        return euclidean_algorithm(y, r)


print(euclidean_algorithm(x, y))


# while文をで解く方法
x, y = map(int, input().split())
while y:
    x, y = y, x % y
print(x)
