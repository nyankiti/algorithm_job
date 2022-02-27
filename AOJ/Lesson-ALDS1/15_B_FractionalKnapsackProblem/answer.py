from sys import stdin

N, W = map(int, stdin.readline().split())

items = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

# まず、itemsを単価の高い順番に並べる
items.sort(key=lambda x: -(x[0] / x[1]))

result = 0
prev_weight = 0

for item in items:
    v, w = item

    if prev_weight + w <= W:
        result += v
    else:
        available_weight = W - prev_weight
        if available_weight < 0:
            break
        result += v * (available_weight/w)

    prev_weight += w

print(result)
